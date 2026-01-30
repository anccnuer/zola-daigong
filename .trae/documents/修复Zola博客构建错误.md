# 修复Zola博客构建错误

## 问题分析

根据错误信息，Zola v0.22.1版本不支持在config.toml根级别使用`paginate_by`字段。错误信息明确指出：

```
ERROR TOML parse error at line 16, column 1
   |
16 | paginate_by = 10
   | ^^^^^^^^^^^
unknown field `paginate_by`, expected one of `base_url`, `theme`, `title`, `description`, `default_language`, `languages`, `translations`, `generate_feeds`, `feed_limit`, `feed_filenames`, `hard_link_static`, `taxonomies`, `taxonomy_root`, `author`, `compile_sass`, `minify_html`, `build_search_index`, `ignored_content`, `ignored_static`, `mode`, `output_dir`, `preserve_dotfiles_in_output`, `link_checker`, `slugify`, `search`, `markdown`, `extra`, `generate_sitemap`, `generate_robots_txt`, `exclude_paginated_pages_in_sitemap`
```

## 解决方案

1. **从config.toml中移除`paginate_by`字段**：删除第16行的`paginate_by = 10`配置

2. **在section级别添加分页配置**：在`content/posts/_index.md`文件的front matter中添加`paginate_by = 10`配置

3. **验证修复**：重新运行`zola build`命令，确认构建成功

## 技术说明

在Zola的早期版本中，分页配置需要在section级别设置，而不是在全局配置中。这样，不同的section可以有不同的分页设置，更加灵活。通过将分页配置移到`content/posts/_index.md`文件中，我们可以保持分页功能的完整性，同时解决构建错误。