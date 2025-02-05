export default {
  router: {
    Chat: '最近对话',
    History: '对话历史',
    DatabaseChat: '数据库配置'
  },
  dashboard: {
    title: 'SQL方言转换助手',
    subtitle: '让跨数据库迁移变得简单高效',
    github: '在 GitHub 上查看项目',
    features: {
      title: '功能特点',
      format: {
        title: '多格式支持',
        desc: '支持处理和分析文本、PDF等各种非结构化数据，提供统一的分析接口。'
      },
      nlp: {
        title: '自然语言交互',
        desc: '使用大语言模型技术，支持用自然语言描述分析需求，无需专业技能。'
      },
      engine: {
        title: '智能分析引擎',
        desc: '基于LLM，自动理解查询意图，生成优化执行计划，确保分析准确性。'
      },
      database: {
        title: '多数据库支持',
        desc: '支持MySQL、PostgreSQL、Oracle等主流数据库。提供SQL语法解析和转换支持，能够处理复杂查询、存储过程等多种SQL语句。'
      },
      conversion: {
        title: '智能转换',
        desc: '采用AI技术智能分析SQL语句结构，自动处理不同数据库间的语法差异。支持批量转换，提升迁移效率。'
      },
      validation: {
        title: '执行计划验证',
        desc: '自动对比转换前后的SQL执行计划，确保性能一致性。内置优化策略，针对不同数据库特性进行优化。'
      }
    },
    operation: {
      title: '开始对话',
      subtitle: '选择模型和文档集合开始您的智能分析之旅',
      model: '对话模型',
      modelPlaceholder: '请选择模型',
      kb: '文档集合',
      kbPlaceholder: '请选择文档集合',
      input: '请输入您的问题',
      submit: '开始分析',
      sourceDb: {
        label: '来源数据库',
        placeholder: '请选择来源数据库'
      },
      targetDb: {
        label: '目标数据库',
        placeholder: '请选择目标数据库',
        search: '搜索数据库名称',
        add: '添加配置'
      },
      sql: {
        placeholder: '请输入需要转换的SQL语句...'
      },
      convert: '开始转换',
      validation: {
        noSql: '请输入要改写的SQL语句',
        noSource: '请选择来源数据库',
        noTarget: '请选择目标数据库'
      }
    },
    error: {
      modelList: '获取模型列表失败',
      kbList: '获取文档集合列表失败',
      incomplete: '请完善所有信息',
      submit: '提交问题失败'
    },
    dialog: {
      add: {
        title: '添加数据库配置',
        cancel: '取消',
        confirm: '保存'
      }
    }
  },
  layout: {
    navbar: {
      home: '首页',
      github: 'Github',
      loginOut: '退出登录',
      logoutSuccess: '退出登录成功'
    },
    tagsView: {
      refresh: '刷新',
      close: '关闭',
      closeOthers: '关闭其他',
      closeAll: '关闭所有'
    },
    breadcrumb: {
      dashboard: '首页'
    },
    title: '数据库语句转换系统',
    sidebar: {
      logo: {
        title: '数据库语句转换'
      },
      tooltip: {
        collapse: '收起侧边栏',
        expand: '展开侧边栏',
        newChat: '开始新的转换',
        feedback: '我们非常期待您的反馈！',
        github: '前往Github，给我们一个Star吧！鼓励是前进的动力，我们一定会做的更好的！🎉🎉🎉',
        language: '切换语言',
        theme: '切换主题',
        logoutConfirm: '确定要退出登录吗？'
      }
    }
  },
  menu: {
    dashboard: '首页',
    chat: '最近改写',
    history: '改写历史',
    knowledge: '知识库',
    database: '数据库配置',
    models: '模型管理',
    tooltip: {
      chat: '查看最近一次改写',
      history: '查看改写历史',
      knowledge: '查看知识库',
      database: '进行数据库配置',
      models: '进行模型配置'
    }
  },
  sidebar: {
    logo: {
      title: 'Unify System'
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
  tour: {
    welcome: {
      title: '👋 欢迎使用智能分析系统',
      desc: '这是一个强大的非结构化数据分析平台，帮助您快速理解和分析各类文本数据。'
    },
    dashboard: {
      title: '功能：开始新对话',
      desc: '在这里您可以开始一个新的数据分析任务。'
    },
    chat: {
      title: '功能：最近对话',
      desc: '查看您最近的对话记录，包括对话内容和分析结果。'
    },
    history: {
      title: '功能：分析历史',
      desc: '查看所有历史分析记录，包括文本分析结果和对话记录，方便回顾和复用。'
    },
    knowledge: {
      title: '功能：数据集管理',
      desc: '管理所有数据集，包括文档导入、查看和删除操作。'
    },
    models: {
      title: '功能：模型管理',
      desc: '管理所有模型，包括模型导入、查看和删除操作。'
    },
    llm: {
      title: '功能：选择LLM模型',
      desc: '选择您想要使用的LLM模型，支持多种模型选项。'
    },
    kb: {
      title: '功能：选择文档集',
      desc: '选择您想要使用的文档集，支持多个文档集选项。'
    },
    input: {
      title: '文本输入区',
      desc: '在这里输入您想要分析的文本内容。'
    },
    convert: {
      title: '功能：开始分析',
      desc: '点击按钮开始智能分析，系统将自动处理文本并生成分析报告。'
    },
    github: {
      title: '开源社区',
      desc: '本项目在GitHub开源。欢迎加入社区，一起完善系统。'
    }
  },
  history: {
    title: '改写历史',
    search: {
      placeholder: '搜索SQL语句',
      clear: '清除搜索'
    },
    empty: {
      title: '暂无改写记录',
      description: '还没有任何SQL改写记录',
      noResults: '没有找到匹配的改写记录',
      subText: '前往首页开始您的第一次SQL改写',
      button: '开始改写'
    },
    list: {
      detail: '详情',
      loading: '加载中'
    },
    status: {
      success: '成功',
      failed: '失败',
      processing: '处理中'
    },
    dialog: {
      title: '改写详情'
    }
  },
  knowledge: {
    title: '知识库列表',
    detail: {
      back: '返回',
      dataCount: '数据数量',
      addNewFile: '添加新文件',
      searchPlaceholder: '请输入搜索内容',
      menu: {
        dataset: '数据集',
        search: '搜索测试',
        setting: '配置'
      },
      steps: {
        selectFile: '选择文件',
        process: '数据处理',
        addQueue: '添加任务队列'
      },
      card: {
        description: '描述：',
        tree: '语法树：',
        detail: '详细信息：'
      },
      status: {
        completed: '已完成',
        pending: '待处理',
        processing: '处理中',
        failed: '失败',
        error: '错误'
      },
      error: {
        reason: '失败原因: {msg}',
        getDetail: '获取知识库详情失败',
        search: '搜索失败',
        processFile: '处理文件失败: {msg}'
      },
      retry: '重试',
      delete: {
        confirmText: '此操作将删除文档及其对应的向量数据，且无法恢复。',
        title: '确认删除？',
        success: '文档删除成功',
        error: '文档删除失败'
      },
      chunks: {
        title: '文档分块详情',
        block: '分块'
      },
      settings: {
        name: '名称',
        description: '描述',
        embeddingModel: '向量模型',
        delete: '删除',
        deleteConfirm: '删除数据集将同时删除所有文档和向量数据。此操作无法撤销。是否继续？',
        deleteTitle: '删除数据集',
        deleteSuccess: '删除成功'
      },
      table: {
        fileName: '文件名',
        splitMethod: '分割方法',
        fileSize: '文件大小',
        addTime: '添加时间',
        status: '状态'
      },
      form: {
        name: '名称',
        description: '介绍',
        embeddingModel: '向量模型',
        databaseType: '数据库类型',
        operator: '操作符',
        link: '链接',
        tree: '语法树',
        detail: '详细信息'
      },
      dialog: {
        edit: {
          title: '编辑数据',
          operator: '操作符',
          description: '描述',
          link: '链接',
          tree: '语法树',
          detail: '详细信息',
          cancel: '取消',
          confirm: '确认'
        },
        add: {
          title: '添加新知识',
          loading: '正在添加...',
          cancel: '取消',
          confirm: '确认'
        },
        delete: {
          title: '警告',
          confirmMessage: '确定要删除这条数据吗？',
          success: '删除成功',
          error: '删除失败'
        }
      },
      message: {
        updateSuccess: '更新成功',
        updateError: '更新失败',
        addSuccess: '添加成功',
        addError: '添加失败',
        retrySuccess: '已重新提交处理',
        retryError: '重试失败',
        deleteKbConfirm: '删除知识库将同时删除所有文档和向量数据，此操作不可恢复，是否继续？',
        deleteKbTitle: '删除知识库',
        deleteKbSuccess: '删除成功'
      },
      search: {
        title: '搜索结果展示（近似值评分为百分制，分数越高，相关性越高，100最高。）',
        result: '结果',
        score: '评分：',
        docFormat: '文档格式',
        splitIndex: '文本分割序号'
      },
      button: {
        delete: '删除',
        retry: '重新处理'
      },
      next: '下一步',
      complete: '完成'
    },
    error: {
      list: 'Failed to get document collection list:'
    },
    create: {
      modelConfig: '模型配置',
      submit: '创建',
      success: '创建成功',
      error: '创建失败',
      button: '创建知识库',
      title: '创建知识库',
      fetchError: '获取模型列表失败',
      form: {
        name: '知识库名称',
        namePlaceholder: '请输入知识库名称',
        description: '描述',
        descriptionPlaceholder: '请输入描述',
        embeddingModel: '向量模型',
        embeddingModelPlaceholder: '请选择向量模型',
        dimension: '维度',
        databaseType: '数据库类型',
        databaseTypePlaceholder: '请选择数据库类型'
      },
      rules: {
        nameRequired: '请输入知识库名称',
        nameLength: '长度应为2-50个字符',
        embeddingRequired: '请选择向量模型',
        databaseTypeRequired: '请选择数据库类型'
      },
      tour: {
        title: '创建知识库',
        desc: '点击这里创建一个新的知识库'
      }
    },
    import: {
      json: '导入JSON文件',
      single: '添加单条数据',
      search: {
        placeholder: '请输入搜索内容',
        button: '搜索'
      },
      title: '导入知识库',
      prevStep: '上一步',
      steps: {
        selectFile: '选择文件',
        processData: '数据处理',
        addToQueue: '添加任务队列'
      },
      upload: {
        text: '点击或拖动JSON文件到此处',
        tip: '仅支持JSON格式文件，文件内容需要是数组格式',
        limit: '最多支持 15 个文件',
        exceed: '最多只能上传15个文件'
      },
      fileList: {
        name: '文件名',
        progress: '解析进度',
        count: '数据条数',
        items: '条',
        action: '操作',
        delete: '删除'
      },
      card: {
        title: '数据预览',
        count: '条',
        edit: '编辑',
        delete: '删除',
        description: '描述',
        tree: '语法树',
        detail: '详细信息'
      },
      process: {
        title: '数据处理配置',
        splitMethod: '分割方法',
        normalSplit: '普通分割',
        normalSplitTip: '按字符数和特定符号进行分割。',
        aiSplit: 'AI分割',
        aiSplitTip: '使用AI进行智能文档分割，会消耗AI令牌。'
      },
      button: {
        processData: '处理数据',
        addToQueue: '添加到队列',
        complete: '完成',
        next: '下一步',
        upload: '上传'
      },
      preview: {
        title: '数据预览与编辑',
        count: '条',
        edit: '编辑',
        delete: '删除'
      },
      complete: {
        message: '数据已添加到队列，将在 {countdown} 秒后跳转。'
      },
      errors: {
        unsupportedType: '不支持的文件类型：{type}',
        fileTooLarge: '文件大小超出限制：{name}',
        uploadFailed: '上传失败',
        deleteFailed: '删除失败',
        processFailed: '处理失败',
        processSuccess: '处理成功'
      }
    }
  },
  models: {
    add: {
      llm: '添加LLM模型',
      embedding: '添加Embedding模型'
    },
    tabs: {
      llm: 'LLM模型',
      embedding: 'Embedding模型'
    },
    deploymentType: {
      cloud: '云端',
      local: '本地',
      cloudModel: '云端模型',
      localModel: '本地模型'
    },
    status: {
      active: '启用中',
      inactive: '已禁用'
    },
    dialog: {
      add: '添加模型',
      edit: '编辑模型'
    },
    form: {
      name: '模型名称',
      deploymentType: '部署类型',
      path: '模型路径',
      apiBase: 'API地址',
      apiKey: 'API密钥',
      temperature: '温度',
      maxTokens: '最大Token',
      dimension: '向量维度',
      description: '描述',
      status: '状态'
    },
    placeholder: {
      apiBase: '未设置API地址',
      path: '未设置模型路径',
      notSet: '未设置',
      noDesc: '暂无描述'
    },
    info: {
      temperature: '温度: {value}',
      maxTokens: '最大Token: {value}',
      dimension: '向量维度: {value}'
    },
    tooltip: {
      edit: '编辑模型',
      delete: '删除模型'
    },
    message: {
      deleteConfirm: '确定要删除该模型吗？',
      deleteSuccess: '删除成功',
      deleteError: '删除失败',
      updateSuccess: '更新成功',
      createSuccess: '创建成功',
      updateError: '更新失败',
      createError: '创建失败',
      fetchError: '获取{type}模型列表失败'
    },
    rules: {
      name: {
        required: '请输入模型名称',
        length: '长度在2到100个字符'
      },
      deploymentType: '请选择部署类型',
      path: '请输入模型路径',
      apiBase: '请输入API地址',
      dimension: '请输入向量维度'
    }
  },
  common: {
    cancel: '取消',
    confirm: '确认',
    tip: '提示'
  },
  chat: {
    empty: {
      title: '暂无改写记录',
      description: '还没有任何SQL改写记录',
      subText: '前往首页开始您的第一次SQL改写',
      button: '开始改写'
    },
    status: {
      success: '成功',
      failed: '失败',
      processing: '处理中'
    }
  },
  database: {
    title: '数据库配置列表',
    create: {
      button: '创建新的配置',
      title: '创建数据库配置',
      edit: '编辑数据库配置'
    },
    search: {
      placeholder: '搜索数据库名称'
    },
    info: {
      username: '用户名',
      port: '端口',
      database: '数据库',
      service: 'service'
    },
    action: {
      edit: '编辑',
      delete: '删除',
      save: '保存',
      cancel: '取消'
    },
    message: {
      deleteConfirm: '确定要删除该数据库配置吗？',
      deleteSuccess: '删除成功',
      deleteError: '删除失败',
      saveSuccess: '保存成功',
      updateSuccess: '更新成功',
      saveError: '保存失败',
      warning: '警告'
    },
    form: {
      host: '主机地址',
      hostPlaceholder: '请输入主机地址',
      username: '用户名',
      usernamePlaceholder: '请输入用户名',
      password: '密码',
      passwordPlaceholder: '请输入密码',
      database: '数据库',
      databasePlaceholder: '请输入数据库名称',
      port: '端口',
      portPlaceholder: '请输入端口号',
      type: '数据库类型',
      typePlaceholder: '请选择数据库类型',
      description: '描述',
      descriptionPlaceholder: '请输入描述信息',
      types: {
        mysql: 'MySQL',
        oracle: 'Oracle'
      }
    },
    rules: {
      host: '请输入主机地址',
      username: '请输入用户名',
      password: '请输入密码',
      database: '请输入数据库名称',
      port: '请输入端口号',
      type: '请选择数据库类型'
    }
  },
  login: {
    title: '登录',
    form: {
      username: '用户名',
      usernamePlaceholder: '请输入用户名',
      password: '密码',
      passwordPlaceholder: '请输入密码'
    },
    button: '登录',
    rules: {
      username: '用户名不能为空',
      password: '密码不能为空'
    },
    success: '登录成功',
    error: '登录失败'
  }
}
