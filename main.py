# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: main
# @Author: xxxx
# @Time: 2025/3/1 23:36

import argparse

# from cracksql.translate import run_cracksql_translation
from cracksql.init_knowledge_base import initialize_kb
from cracksql.utils.constants import DIALECT_LIST


def parse_run_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Run Local to Global Dialect Translation.')

    parser.add_argument('--config_name', type=str,
                        default='PRODUCTION', help='Configuration app name')
    parser.add_argument('--config_file', type=str,
                        default='./config/config.yaml', help='Configuration file path')

    parser.add_argument('--src_dialect', type=str,
                        help='Source database dialect', choices=DIALECT_LIST)
    parser.add_argument('--tgt_dialect', type=str,
                        help='Target database dialect', choices=DIALECT_LIST)
    parser.add_argument('--src_sql', type=str,
                        help='Source SQL to be translated or file including multiple Source SQLs')

    parser.add_argument('--src_kb_name', type=str,
                        help='Source specification base or its file path')
    parser.add_argument('--tgt_kb_name', type=str,
                        help='Target specification base or its file path')

    parser.add_argument('--llm_model_name', type=str,
                        help='LLM for dialect translation')

    parser.add_argument('--retrieval_on', action='store_true',
                        help='Employ specification retrieval for dialect translation')
    parser.add_argument('--top_k', type=int, default=3,
                        help='Number of retrieved specification')
    parser.add_argument('--max_retry_time', type=int, default=2,
                        help='Maximal translation attempts for one segment')

    parser.add_argument('--out_dir', type=str, default=None,
                        help='Output directory to dump translation result')

    return parser.parse_args()


if __name__ == "__main__":
    config_file = "./base_config/config/init_config.yaml"
    initialize_kb(config_file, init_all=True)

    # args = parse_run_args()
    # translated_sql, model_ans_list, \
    # used_pieces, lift_histories = run_cracksql_translation(args.src_dialect, args.tgt_dialect, args.src_sql, args.llm_model_name,
    #                                                        retrieval_on=args.retrieval_on, top_k=args.top_k,
    #                                                        max_retry_time=args.max_retry_time,
    #                                                        out_type="file", out_dir=args.out_dir)
    # print(translated_sql)
