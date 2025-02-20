const TOUR_OPTIONS_KEY = 'tour-options';
const WEBSITE_FIRST_SHOW_KEY = 'website-first-show';
const KNOWLEDGE_FIRST_SHOW_KEY = 'knowledge-first-show';

function getLocalStorageOptions() {
  return JSON.parse(localStorage.getItem(TOUR_OPTIONS_KEY)) || {};
}

function saveLocalStorageOptions(options) {
  localStorage.setItem(TOUR_OPTIONS_KEY, JSON.stringify(options));
}

// 检查是否是首次访问
export const hasWebsiteBeenShownFirstTime = () => {
  const tourOptions = getLocalStorageOptions();
  return !!tourOptions[WEBSITE_FIRST_SHOW_KEY];
}

// 设置首次访问状态
export const setWebsiteFirstShowStatus = (status) => {
  const tourOptions = getLocalStorageOptions();
  tourOptions[WEBSITE_FIRST_SHOW_KEY] = status;
  saveLocalStorageOptions(tourOptions);
}

export const hasKnowledgeBeenShownFirstTime = () => {
  const tourOptions = getLocalStorageOptions();
  return !!tourOptions[KNOWLEDGE_FIRST_SHOW_KEY];
}

export const setKnowledgeFirstShowStatus = (status) => {
  const tourOptions = getLocalStorageOptions();
  tourOptions[KNOWLEDGE_FIRST_SHOW_KEY] = status;
  saveLocalStorageOptions(tourOptions);
}
