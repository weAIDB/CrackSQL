export default {
  router: {
    Chat: 'Recent Chat',
    History: 'Chat History',
    DatabaseChat: 'Database Configuration'
  },
  dashboard: {
    title: 'SQL Dialect Converter',
    subtitle: 'Making cross-database migration simple and efficient',
    github: 'View on GitHub',
    operation: {
      title: 'Start Conversation',
      subtitle: 'Select model and database to start your SQL dialect rewrite journey',
      model: 'Conversation Model',
      modelPlaceholder: 'Please select a model',
      kb: 'Database',
      kbPlaceholder: 'Please select a database',
      input: 'Please enter your SQL statement',
      submit: 'Start Rewrite',
      sourceDb: {
        label: 'Source Database',
        placeholder: 'Please select'
      },
      sourceKb: {
        label: 'Knowledge Base Associated with Source Database',
        placeholder: 'Please select'
      },
      targetKb: {
        label: 'Knowledge Base Associated with Target Database',
        placeholder: 'Please select'
      },
      llmModel: {
        label: 'LLM Model',
        placeholder: 'Please select'
      },
      targetDb: {
        label: 'Target Database',
        placeholder: 'Please select',
        search: 'Search database name',
        add: 'Add Configuration'
      },
      sql: {
        placeholder: 'Please enter the SQL statement to convert...'
      },
      convert: 'Start Conversion',
      validation: {
        noSql: 'Please enter SQL statement',
        noSource: 'Please select source database',
        noTarget: 'Please select target database'
      }
    },
    error: {
      modelList: 'Failed to get model list',
      kbList: 'Failed to get document collection list',
      incomplete: 'Please complete all information',
      submit: 'Failed to submit question'
    },
    dialog: {
      add: {
        title: 'Add Database Configuration',
        cancel: 'Cancel',
        confirm: 'Save'
      }
    }
  },
  layout: {
    navbar: {
      home: 'Home',
      github: 'Github',
      loginOut: 'Log Out',
      logoutSuccess: 'Logout successful'
    },
    tagsView: {
      refresh: 'Refresh',
      close: 'Close',
      closeOthers: 'Close Others',
      closeAll: 'Close All'
    },
    breadcrumb: {
      dashboard: 'Dashboard'
    },
    title: 'SQL Dialect Rewrite',
    sidebar: {
      logo: {
        title: 'SQL Dialect Rewrite'
      },
      tooltip: {
        collapse: 'Collapse Sidebar',
        expand: 'Expand Sidebar',
        newChat: 'Start New Conversion',
        feedback: 'We look forward to your feedback!',
        github: 'Visit Github and give us a Star! Your encouragement drives us forward! 🎉🎉🎉',
        language: 'Switch Language',
        theme: 'Switch Theme',
        logoutConfirm: 'Are you sure you want to log out?'
      }
    }
  },
  menu: {
    dashboard: 'Dashboard',
    chat: 'Recent Rewrite',
    history: 'Rewrite History',
    knowledge: 'Knowledge Base',
    database: 'Database Config',
    models: 'Model Management',
    tooltip: {
      chat: 'View recent rewrite task',
      history: 'View rewrite history',
      knowledge: 'Manage knowledge base',
      database: 'Configure target database',
      models: 'Configure LLM and Embedding models'
    }
  },
  sidebar: {
    logo: {
      title: 'SQL Dialect Rewrite'
    },
    tooltip: {
      collapse: 'Collapse Sidebar',
      expand: 'Expand Sidebar',
      newChat: 'Start New Chat',
      feedback: 'We look forward to your feedback!',
      github: 'Visit Github and give us a Star! Your encouragement drives us forward! 🎉🎉🎉',
      language: 'Switch Language',
      theme: 'Switch Theme',
      logoutConfirm: 'Are you sure you want to log out?'
    }
  },
  history: {
    title: 'Rewrite History',
    search: {
      placeholder: 'Search SQL statements',
      clear: 'Clear Search'
    },
    delete: {
      title: 'Delete Rewrite Record',
      confirm: 'Are you sure you want to delete this rewrite record?',
      success: 'Delete successful',
      error: 'Delete failed'
    },
    empty: {
      title: 'No Rewrite Records',
      description: 'No SQL rewrite records yet',
      noResults: 'No matching rewrite records found',
      subText: 'Go to homepage to start your first SQL rewrite',
      button: 'Start Rewrite'
    },
    list: {
      detail: 'Details',
      loading: 'Loading'
    },
    status: {
      success: 'Success',
      failed: 'Failed',
      processing: 'Processing'
    },
    dialog: {
      title: 'Rewrite Details'
    }
  },
  knowledge: {
    title: 'Knowledge Base List',
    empty: {
      title: 'No Knowledge Base',
      description: 'No knowledge base yet',
      button: 'Create Knowledge Base'
    },
    detail: {
      table: {
        fileName: 'File Name',
        splitMethod: 'Split Method',
        fileSize: 'File Size',
        addTime: 'Add Time',
        status: 'Status'
      },
      status: {
        completed: 'Completed',
        pending: 'Pending',
        processing: 'Processing',
        failed: 'Failed',
        error: 'Error'
      },
      error: {
        reason: 'Failure reason: {msg}',
        getDetail: 'Failed to get knowledge base details',
        search: 'Search failed',
        processFile: 'Failed to process file: {msg}'
      },
      retry: 'Retry',
      delete: {
        confirmText: 'This operation will delete both the document and its corresponding vectors, and cannot be recovered.',
        title: 'Confirm Delete?',
        success: 'Document deleted successfully',
        error: 'Failed to delete document'
      },
      back: 'Back',
      dataCount: 'Total Data',
      addNewFile: 'Add New File',
      searchPlaceholder: 'Enter search content',
      menu: {
        dataset: 'Dataset',
        search: 'Search Test',
        setting: 'Settings'
      },
      steps: {
        selectFile: 'Select File',
        process: 'Process Data',
        addQueue: 'Add to Queue'
      },
      upload: {
        text: 'Click or drag JSON file here',
        tip: 'Only JSON files are supported, file content must be array format',
        limit: 'Maximum 15 files',
        exceed: 'Maximum 15 files allowed'
      },
      preview: {
        title: 'Data Preview and Edit',
        count: 'items'
      },
      card: {
        description: 'Description:',
        tree: 'Syntax Tree:',
        detail: 'Details:',
        edit: 'Edit',
        delete: 'Delete'
      },
      chunks: {
        title: 'Document Chunks Details',
        block: 'Block'
      },
      settings: {
        name: 'Name',
        description: 'Description',
        embeddingModel: 'Embedding Model',
        delete: 'Delete',
        deleteConfirm: 'Deleting the data collection will also delete all documents and vector data. This operation cannot be undone. Do you want to continue?',
        deleteTitle: 'Delete Data Collection',
        deleteSuccess: 'Delete successful'
      },
      form: {
        name: 'Name',
        description: 'Description',
        embeddingModel: 'Embedding Model',
        databaseType: 'Database Type',
        operator: 'Operator',
        link: 'Link',
        tree: 'Syntax Tree',
        detail: 'Details'
      },
      dialog: {
        edit: {
          title: 'Edit Data',
          operator: 'Operator',
          description: 'Description',
          link: 'Link',
          tree: 'Syntax Tree',
          detail: 'Details',
          cancel: 'Cancel',
          confirm: 'Confirm'
        },
        add: {
          title: 'Add New Knowledge',
          loading: 'Adding...',
          cancel: 'Cancel',
          confirm: 'Confirm'
        },
        delete: {
          title: 'Warning',
          confirmMessage: 'Are you sure you want to delete this item?',
          success: 'Delete successful',
          error: 'Delete failed'
        }
      },
      message: {
        updateSuccess: 'Update successful',
        updateError: 'Update failed',
        addSuccess: 'Add successful',
        addError: 'Add failed',
        retrySuccess: 'Successfully resubmitted for processing',
        retryError: 'Retry failed',
        deleteKbConfirm: 'Deleting the knowledge base will also delete all documents and vector data. This operation cannot be undone. Do you want to continue?',
        deleteKbTitle: 'Delete Knowledge Base',
        deleteKbSuccess: 'Delete successful',
        keywordRequired: 'Please enter keyword',
        typeRequired: 'Please select type',
        detailRequired: 'Please enter detail',
        descriptionRequired: 'Please enter description',
        treeRequired: 'Please enter tree'
      },
      search: {
        title: 'Search Results (Similarity score is percentile, higher score means more relevant, 100 is maximum.)',
        result: 'Result',
        score: 'Score:',
        docFormat: 'Document Format',
        splitIndex: 'Split Index'
      },
      button: {
        delete: 'Delete',
        retry: 'Retry',
        save: 'Save'
      },
      next: 'Next',
      complete: 'Complete'
  
    },
    error: {
      list: 'Failed to get document collection list:'
    },
    create: {
      tour: {
        title: 'Create Knowledge Base',
        desc: 'Click here to create a new knowledge base'
      },
      button: 'Create Knowledge Base',
      title: 'Create Knowledge Base',
      modelConfig: 'Model Configuration',
      submit: 'Create',
      success: 'Created successfully',
      error: 'Creation failed',
      fetchError: 'Failed to get model list',
      form: {
        name: 'Knowledge Base Name',
        namePlaceholder: 'Please enter knowledge base name',
        description: 'Description',
        descriptionPlaceholder: 'Please enter description',
        embeddingModel: 'Embedding Model',
        embeddingModelPlaceholder: 'Please select embedding model',
        dimension: 'Dimension',
        databaseType: 'Database Type',
        databaseTypePlaceholder: 'Please select database type'
      },
      rules: {
        nameRequired: 'Please enter knowledge base name',
        nameLength: 'Length should be 2 to 50 characters',
        embeddingRequired: 'Please select embedding model',
        databaseTypeRequired: 'Please select database type'
      }
    },
    import: {
      json: 'Import JSON File',
      single: 'Add Single Item',
      addQueue: 'Add task queue, will redirect back to knowledge list in {countdown} seconds.',
      search: {
        placeholder: 'Please enter search content',
        button: 'Search'
      },
      button: {
        next: 'Next',
        upload: 'Upload',
        complete: 'Complete',
        process: 'Process'
      },
      prevStep: 'Previous',
      nextStep: 'Next',
      steps: {
        selectFile: 'Select Files',
        processData: 'Process Data',
        addToQueue: 'Add to Queue'
      },
      upload: {
        text: 'Click or drag JSON file here',
        tip: 'Only JSON files are supported, file content must be array format',
        limit: 'Maximum 15 files',
        exceed: 'Maximum 15 files allowed'
      },
      fileList: {
        name: 'File Name',
        progress: 'Parse Progress',
        count: 'Data Count',
        items: 'items',
        action: 'Action',
        delete: 'Delete'
      },
      card: {
        description: 'Description:',
        tree: 'Syntax Tree:',
        detail: 'Details:',
        edit: 'Edit',
        delete: 'Delete',
        preview: 'Preview'
      },
      process: {
        title: 'Data Processing Configuration',
        splitMethod: 'Split Method',
        normalSplit: 'Normal Split',
        normalSplitTip: 'Split by character count and specific symbols.',
        aiSplit: 'AI Split',
        aiSplitTip: 'Use AI for intelligent document splitting, will consume AI tokens.'
      },
      buttons: {
        processData: 'Process Data',
        addToQueue: 'Add to Queue',
        complete: 'Complete',
        next: 'Next'
      },
      preview: {
        title: 'Data Preview and Edit',
        count: 'items',
        edit: 'Edit',
        delete: 'Delete'
      },
      complete: {
        message: 'Data has been added to the queue, will redirect in {countdown} seconds.'
      },
      errors: {
        unsupportedType: 'Unsupported file type: {type}',
        fileTooLarge: 'File size exceeds limit: {name}',
        uploadFailed: 'Upload failed',
        deleteFailed: 'Delete failed',
        processFailed: 'Process failed',
        processSuccess: 'Process successful'
      }
    }
  },
  models: {
    add: {
      llm: 'Add LLM Model',
      embedding: 'Add Embedding Model'
    },
    tabs: {
      llm: 'LLM Models',
      embedding: 'Embedding Models'
    },
    deploymentType: {
      cloud: 'Cloud',
      local: 'Local',
      cloudModel: 'Cloud Model',
      localModel: 'Local Model'
    },
    status: {
      active: 'Active',
      inactive: 'Inactive'
    },
    dialog: {
      add: 'Add Model',
      edit: 'Edit Model'
    },
    form: {
      name: 'Model Name',
      deploymentType: 'Deployment Type',
      path: 'Model Path',
      apiBase: 'API Base',
      apiKey: 'API Key',
      temperature: 'Temperature',
      maxTokens: 'Max Tokens',
      dimension: 'Dimension',
      description: 'Description',
      status: 'Status'
    },
    placeholder: {
      apiBase: 'API address not set',
      path: 'Model path not set',
      notSet: 'Not set',
      noDesc: 'No description'
    },
    info: {
      temperature: 'Temperature: {value}',
      maxTokens: 'Max Tokens: {value}',
      dimension: 'Vector Dimension: {value}'
    },
    tooltip: {
      edit: 'Edit Model',
      delete: 'Delete Model'
    },
    message: {
      deleteConfirm: 'Are you sure you want to delete this model?',
      deleteSuccess: 'Delete successful',
      deleteError: 'Delete failed',
      updateSuccess: 'Update successful',
      createSuccess: 'Create successful',
      updateError: 'Update failed',
      createError: 'Create failed',
      fetchError: 'Failed to get {type} model list'
    },
    rules: {
      name: {
        required: 'Please enter model name',
        length: 'Length should be 2 to 100 characters'
      },
      deploymentType: 'Please select deployment type',
      path: 'Please enter model path',
      apiBase: 'Please enter API address',
      dimension: 'Please enter vector dimension'
    }
  },
  common: {
    cancel: 'Cancel',
    confirm: 'Confirm',
    tip: 'Tip'
  },
  chat: {
    empty: {
      title: 'No Rewrite Records',
      description: 'No SQL rewrite records yet',
      subText: 'Go to homepage to start your first SQL rewrite',
      button: 'Start Rewrite'
    },
    status: {
      success: 'Success',
      failed: 'Failed',
      processing: 'Processing'
    }
  },
  database: {
    title: 'Database Configuration List',
    create: {
      button: 'Create New Configuration',
      title: 'Create Database Configuration',
      edit: 'Edit Database Configuration'
    },
    search: {
      placeholder: 'Search database name'
    },
    info: {
      username: 'Username',
      port: 'Port',
      database: 'Database',
      service: 'Service'
    },
    action: {
      edit: 'Edit',
      delete: 'Delete',
      save: 'Save',
      cancel: 'Cancel'
    },
    message: {
      deleteConfirm: 'Are you sure you want to delete this database configuration?',
      deleteSuccess: 'Delete successful',
      deleteError: 'Delete failed',
      saveSuccess: 'Save successful',
      updateSuccess: 'Update successful',
      saveError: 'Save failed',
      warning: 'Warning'
    },
    form: {
      host: 'Host',
      hostPlaceholder: 'Please enter host address',
      username: 'Username',
      usernamePlaceholder: 'Please enter username',
      password: 'Password',
      passwordPlaceholder: 'Please enter password',
      database: 'Database',
      databasePlaceholder: 'Please enter database name',
      port: 'Port',
      portPlaceholder: 'Please enter port',
      type: 'Database Type',
      typePlaceholder: 'Please select database type',
      description: 'Description',
      descriptionPlaceholder: 'Please enter description',
      types: {
        mysql: 'MySQL',
        oracle: 'Oracle'
      }
    },
    rules: {
      host: 'Please enter host address',
      username: 'Please enter username',
      password: 'Please enter password',
      database: 'Please enter database name',
      port: 'Please enter port',
      type: 'Please select database type'
    }
  },
  login: {
    title: 'Login',
    form: {
      username: 'Username',
      usernamePlaceholder: 'Please enter username',
      password: 'Password',
      passwordPlaceholder: 'Please enter password'
    },
    button: 'Login',
    rules: {
      username: 'Username is required',
      password: 'Password is required'
    },
    success: 'Login successful',
    error: 'Login failed'
  }
}
