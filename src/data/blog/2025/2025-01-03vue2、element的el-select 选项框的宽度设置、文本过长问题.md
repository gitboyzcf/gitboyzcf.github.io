---
author: boyzcf
pubDatetime: 2025-01-03 11:34:13
modDatetime: 2025-01-03 11:34:13
title: vue2、element的el-select 选项框的宽度设置、文本过长问题
slug: 
featured: false
draft: false
tags:
  - 前端
  - Vue
  - 拒绝废话
  - 问题
  - element-ui
  - JavaScript
description:
  vue2、element的el-select 选项框的宽度设置、文本过长问题。
---

![禁止废话](../../../assets/images/pub/jjfh.webp)

![结果](../../../assets/images/2025/e005973a29d04dd88dbbcdb639ffc0d5.gif)

```html
<el-select v-model="value" placeholder="请选择">
  <el-option
    v-for="item in cities"
    :key="item.value"
    :label="item.label"
    :value="item.value">
      <el-tooltip class="item" :content="item.label" placement="right">
     <span>{{ item.label }}</span>
   </el-tooltip>
  </el-option>
</el-select>

<style>
.el-select-dropdown {
  width: 100px;
}
.el-select-dropdown__item {
  width:100%;
  overflow: hidden; 
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
```

```javascript
data() {
  return {
    cities: [{
      value: 'Beijing',
      label: '北京北京北京北京北京北京北京'
    }, {
      value: 'Shanghai',
      label: '上海'
    }, {
      value: 'Nanjing',
      label: '南京'
    }, {
      value: 'Chengdu',
      label: '成都'
    }, {
      value: 'Shenzhen',
      label: '深圳'
    }, {
      value: 'Guangzhou',
      label: '广州'
    }],
    value: ''
  }
}
```
