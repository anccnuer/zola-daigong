import re
import os
import html
import subprocess
from bs4 import BeautifulSoup
import markdown

def markdown_to_text(md_content):
    html_content = markdown.markdown(md_content, extensions=['extra'])
    html_content = html.unescape(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    return ' '.join(soup.stripped_strings)

def extract_chars(directory):
    hanzi_set = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(('.md', '.html')):
                continue
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    text = markdown_to_text(content) if file.endswith('.md') else \
                          BeautifulSoup(content, 'html.parser').get_text()
                    hanzi = re.findall(r'[\u3400-\u4DBF\u4E00-\u9FFF]', text)
                    hanzi_set.update(hanzi)
            except Exception as e:
                print(f"处理失败：{path}，错误：{e}")
    return hanzi_set

# 主流程
if __name__ == "__main__":
    # 汉字提取
    hanzi_set = extract_chars('content')
    
    # 写入汉字文件
    with open('hanzi.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(sorted(hanzi_set)))
    
    # 字体子集生成
    font_path = "Zhuque.woff2"
    output_path = os.path.normpath("static/assets/Zhuque.woff2")
    
    try:
        # 创建输出目录
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 执行fonttools命令
        subprocess.run([
            "fonttools", "subset",
            font_path,
            f"--text-file=hanzi.txt",
            f"--output-file={output_path}",
            "--flavor=woff2"
        ], check=True)
        print("✅ 字体子集生成成功")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 字体处理失败，请检查：{str(e)}")
    except FileNotFoundError:
        print("❌ 未找到fonttools，请先执行：pip install fonttools")
    except Exception as e:
        print(f"❌ 发生意外错误：{str(e)}")