# CrackSQL

This is the code respository of **CrackSQL**, which performs SQL translations among different dialects (e.g., translating SQL written in PostgreSQL into the equivalent ones in MySQL). Specifically, it conducts dialect translations based on the following techniques:

- **(1) Functionality-based Syntax Processing:** divides the entire SQL into syntax elements of specific functionalities, which are further normalized and abstracted to ensure the least translations required for LLM;
- **(2) Model-based Syntax Matching:** employs a novel cross-dialect embedding model to identify and equip LLM with specific translation knowledge, derived from the effectiveness of retrieval-enhanced contrastive learning;
- **(3) Local-to-Global Translation Strategy:** adopts a flexible and dynamic strategy to cope with the circumstances that several syntax elements required to be treated as a whole to obtain the same functionality in the target dialect.

**NOTE:**

**The example of the problem instructions can be found at: `./translator/xxxx_prompt.py`.**

## Project Structure

The followings are the code structure of our **CrackSQL** project, where the critical files are annotated with additional comments.

```shell
CrackSQL/
├── data
│   ├── antlr_gram				# the BNF definitions from ANTLR
│   ├── pretrained_model			# the embedding models for syntax matching
│   ├── processed_document			# the prepared specifications in offline phase
│   │  ├── mysql
│   │  ├── ...
│   │  └── oracle
│   └── revised_g4doc				# the processed BNF definitions
├── doc_process					# the offline phase to prepare specifications
│   ├── ...
│   └── make_tree.py
├── exp_res				# the results of translated SQLs
├── preprocessor			# the implementation of functionality-based processing
│   ├── antlr_parser			# the generation of syntax trees
│   │   ├── ...
│   │   └── oracle_parser 
│   └──  parse_tree.py
│   ├── query_simplifier			# the functionality-based processing operations 
│   │   ├── ...
│   │   ├── load_process.py			# the data loader of different specifications
│   │   ├── normalize.py			# the normalization of SQL
│   └─└── rewrite.py				# the rewrite process of SQL
├── retriever					# the implementation of model-based syntax matching
│   │   ├── ...
│   │   ├── retrieval_model.py		# the implementation of cross-dialect embedding model
│   │   ├── retriever_dataset.py	# the collection of retriever datasets
│   │   ├── train_model.py			# the training of cross-dialect embedding model
│   └─└── vector_db.py				# the implementation of Chroma vector database
├── translator					# the collection of LLM-based translators
│   ├── ...
│   ├── llm_translator.py			# the implementation of LLM-based translators
│   └── translator_prompt.py			# the problem instruction for LLM-based translators
└── utils					# the implementation of typical tools
     ├── ...
     ├── db_connector.py				# the configurations of dialect databases
     └── tools.py					# the collection of typical tools
```


## Setup

- **(1) Create the python virtual environment:** utilize the following script to install the required packages (`requirements.txt`).

```shell
# Create the virtualenv `CrackSQL`
conda create -n CrackSQL python=3.10		 	

# Activate the virtualenv `CrackSQL`
conda activate CrackSQL				

# Install requirements with pip
while read requirement; do pip install $requirement; done < requirements.txt	
```

- **(2) Specify the setup configuration:** fill in the basic configurations in `Config.ini` and the database configurations in `./utils/db_connector.py`.

```shell
[MODE]
seg_on = true        # enable the functionality-based syntax processing
retrieval_on = true	 # enable the model-based syntax matching

...

[API]    # specify your API base and key
gpt_api_base = 'Your API base for GPT'
gpt_api_key = 'Your API key for GPT'

llama3.1_api_base = 'Your API base for Llama3.1'
codellama_api_base = 'Your API base for CodeLlama'

```



## Workflow

A demonstration about how to run and streamline the dialect translation workflow is presented in `main.py`. There are two options:

- **`direct_rewrite`:** input the whole SQL to LLM, without any fine-grained processing;
- **`local_rewrite`:** process the SQL into syntax elements and perform model-based syntax matching during translation.

You also need to specify the path of the embedding model in `translate.py`.

```python

def main():
    top_k = 5			# the number of retrieved specifications
    max_retry_time = 2		# the value of maximal trial

    model_id = "gpt-4o"		# the ID of underlying LLM

    ret_id = "all-MiniLM-L6-v2"		# the ID of underlying embedding model
    db_id = "Chroma"			# the ID of vector database

    db_name = "xxxx_BIRD"		# the name of dialect databases (more in `./utils/db_connector.py`)
    
    # the path of vector database
    db_path = {"func": f"your chroma db path for function",
                "keyword": f"your chroma db path for keyword",
                "type": f"your chroma db path for data type"}		
    
    src_dialect, tgt_dialect = "pg", "mysql"
    translator, retriever, vector_db = init_model(model_id, ret_id, db_id, db_path, top_k, tgt_dialect)
    
    data_load = f"your SQL data load path"
    
    with open(data_load, "r", encoding="utf-8") as file:
        json_pairs = json.loads(file.read())

    trans_res = list()
    for pair in tqdm(json_pairs):
        if src_dialect in pair.keys():
            src_sql = pair[src_dialect]
        else:
            src_sql = pair["src_sql"]

        tgt_sql = str()
        if tgt_dialect in pair.keys():
            tgt_sql = pair[tgt_dialect]
        
        try:
            # OPTION 1: without any processing
            trans_sql, resp_list = direct_rewrite(translator, src_sql, src_dialect, tgt_dialect)
            
            # OPTION 2: method proposed in CrackSQL
            # trans_sql, resp_list, used_pieces, lift_histories = local_rewrite(translator, retriever, vector_db,
            #                                                                     src_sql, src_dialect, tgt_dialect,
            #                                                                     db_name=db_name, top_k=top_k,
            #                                                                     max_retry_time=max_retry_time)

            trans_res.append(
                {"src_sql": src_sql, "tgt_sql": tgt_sql,
                    "trans_sql": trans_sql, "response": resp_list})
        except Exception as e:
            traceback.print_exc()

        
        with open("./exp_res/example.json", "w") as file:
            json.dump(trans_res, file, indent=4)

```



## Reference

**We sincerely appreciate the following projects for their efforts in dialect translation!**

[1] SQLGlot, https://github.com/tobymao/sqlglot.

[2] jOOQ, https://github.com/jOOQ/jOOQ.

[3] SQLines, https://www.sqlines.com/home.

