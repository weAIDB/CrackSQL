class ResponseCode(object):
    Success = 0  # 成功
    Fail = -1  # 失败
    NoResourceFound = 40001  # 未找到资源
    InvalidParameter = 40002  # 参数无效
    FrequentOperation = 40009  # 操作频繁,请稍后再试
    ResourceAlreadyExists = 40010  # 资源已经存在
