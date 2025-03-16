export default {
  router: {
    Chat: '最近对话',
    History: '对话历史',
    DatabaseChat: '数据库配置'
  },
  dashboard: {
    title: 'SQL方言转换助手',
    subtitle: '让跨数据库迁移变得简单高效',
    github: '前往Github，给我们一个Star吧！鼓励是前进的动力，我们一定会做的更好的！🎉🎉🎉',
    operation: {
      title: '开始对话',
      subtitle: '选择模型和数据库开始您的SQL方言转换之旅',
      model: '对话模型',
      modelPlaceholder: '请选择模型',
      kb: '数据库',
      kbPlaceholder: '请选择数据库',
      input: '请输入您的SQL语句',
      submit: '开始转换',
      sourceDb: {
        label: '原句所在数据库',
        placeholder: '请选择'
      },
      sourceKb: {
        label: '原句所在数据库关联的知识库',
        placeholder: '请选择'
      },
      targetKb: {
        label: '语句要转到的数据库关联的知识库',
        placeholder: '请选择'
      },
      llmModel: {
        label: 'LLM模型',
        placeholder: '请选择'
      },
      targetDb: {
        label: '语句要转到该数据库',
        placeholder: '请选择',
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
      title: 'SQL Dialect Rewrite'
    },
    tooltip: {
      collapse: '收起侧边栏',
      expand: '展开侧边栏',
      newChat: '开始新的改写',
      feedback: '我们非常期待您的反馈！',
      github: '前往Github，给我们一个Star吧！鼓励是前进的动力，我们一定会做的更好的！🎉🎉🎉',
      language: '切换语言',
      theme: '切换主题',
      logoutConfirm: '确定要退出登录吗？'
    }
  },
  history: {
    title: '改写历史',
    search: {
      placeholder: '搜索SQL语句',
      clear: '清除搜索'
    },
    delete: {
      title: '删除改写记录',
      confirm: '确定要删除这条改写历史记录吗？',
      success: '删除成功',
      error: '删除失败'
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
      loading: '加载中',
      delete: '删除'
    },
    status: {
      success: '成功',
      failed: '失败',
      processing: '处理中'
    },
    dialog: {
      title: '改写详情'
    },
    delete: {
      title: '删除确认',
      confirm: '确定要删除这条改写历史记录吗？',
      success: '删除成功',
      error: '删除失败'
    }
  },
  knowledge: {
    title: '知识库列表',
    empty: {
      title: '暂无知识库',
      description: '还没有任何知识库',
      button: '创建知识库'
    },
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
        deleteKbSuccess: '删除成功',
        keywordRequired: '请输入关键词',
        typeRequired: '请选择类型',
        detailRequired: '请输入详细信息',
        descriptionRequired: '请输入描述',
        treeRequired: '请输入语法树'
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
        retry: '重新处理',
        save: '保存'
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
      addQueue: '添加任务队列，将在 {countdown} 秒后跳转回知识列表。',
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
        detail: '详细信息',
        preview: '预览'
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
    },
    operation: {
      stop: '停止'
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
