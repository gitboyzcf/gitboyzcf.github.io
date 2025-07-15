export const SITE = {
  website: "https://gitboyzcf.github.io/", // replace this with your deployed domain
  author: "boyzcf",
  profile: "/about",
  desc: "Vue, VuePress, React, Vuex, Vue-router, Vue-cli, Vuepress,Piain, blog, uniapp,uni-app, npm, node, 前端, 移动端, 后端",
  title: "Boyzcf's Blog",
  ogImage: "/mp-og.png",
  lightAndDarkMode: true,
  postPerIndex: 4,
  postPerPage: 4,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  showBackButton: true, // show back button in post detail
  editPost: {
    enabled: false,
    text: "Edit page",
    url: "https://gitboyzcf.github.io/edit/main/",
  },
  dynamicOgImage: true,
  dir: "ltr", // "rtl" | "auto"
  lang: "zh-CN", // html lang code. Set this empty and default will be "en"
  timezone: "Asia/Shanghai", // Default global timezone (IANA format) https://zh.wikipedia.org/wiki/List_of_tz_database_time_zones
} as const;
