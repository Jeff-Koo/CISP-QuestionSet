### Create environemnt and Install necessary package
# python -m venv .venv
# source .venv/bin/activate
# pip install markdown weasyprint

import argparse
import markdown
from weasyprint import HTML

def convert_md_to_beautiful_pdf(md_file_path, output_pdf_path):
    # 1. 讀取 Markdown 內容
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    # 2. 將 MD 轉為 HTML 結構（啟用表格、程式碼高亮等擴充功能）
    html_content = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc'])
    
    # 3. 嵌入專門為非技術人員設計的精美 CSS 樣式
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        /* 頁面基本設定 */
        @page {{
            size: A4;
            margin: 20mm 18mm;
            @bottom-right {{
                content: counter(page);
                font-size: 9pt;
                color: #a0aec0;
            }}
        }}
        
        /* 全局字體與顏色 */
        body {{
            font-family: "PingFang TC", "Microsoft JhengHei", -apple-system, sans-serif;
            line-height: 1.7;
            color: #2d3748;
            font-size: 10.5pt;
        }}
        
        /* 標題樣式：去除生硬的線條，改用現代感優雅設計 */
        h1 {{
            font-size: 22pt;
            color: #1a365d;
            margin-top: 0;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3182ce;
        }}
        h2 {{
            font-size: 15pt;
            color: #2b6cb0;
            margin-top: 30px;
            margin-bottom: 12px;
            border-left: 4px solid #3182ce;
            padding-left: 10px;
        }}
        h3 {{
            font-size: 12pt;
            color: #4a5568;
            margin-top: 20px;
            margin-bottom: 8px;
        }}
        
        /* 段落與列表 */
        p {{
            margin-bottom: 16px;
            text-align: justify;
        }}
        ul, ol {{
            margin-bottom: 16px;
            padding-left: 24px;
        }}
        li {{
            margin-bottom: 6px;
        }}
        
        /* 讓表格變得像報告一樣專業 */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 10pt;
        }}
        th, td {{
            border: 1px solid #e2e8f0;
            padding: 10px 12px;
            text-align: left;
        }}
        th {{
            background-color: #ebf8ff;
            color: #2b6cb0;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f7fafc;
        }}
        
        /* 強調區塊/引言 */
        blockquote {{
            margin: 20px 0;
            padding: 12px 18px;
            background-color: #f7fafc;
            border-left: 4px solid #4a5568;
            color: #4a5568;
            font-style: italic;
        }}
        
        /* 行內微小程式碼/專有名詞隱藏技術感 */
        code {{
            font-family: Consolas, monospace;
            background-color: #edf2f7;
            padding: 2px 5px;
            border-radius: 4px;
            font-size: 9.5pt;
            color: #2d3748;
        }}
        
        /* 大段落程式碼區塊（若有） */
        pre {{
            background-color: #1a202c;
            color: #f7fafc;
            padding: 15px;
            border-radius: 6px;
            overflow: auto;
            font-size: 9.5pt;
        }}
        pre code {{
            background-color: transparent;
            color: inherit;
            padding: 0;
        }}
    </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # 4. 輸出為 PDF
    HTML(string=full_html).write_pdf(output_pdf_path)
    print(f"轉換成功！PDF 已儲存至: {output_pdf_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('input', nargs='?', default='input.md', help='input Markdown file (default: input.md)')
    parser.add_argument('output', nargs='?', default='output.pdf', help='output PDF file (default: output.pdf)')
    args = parser.parse_args()
    convert_md_to_beautiful_pdf(args.input, args.output)


### 查看說明
# python convert-md-pdf.py --help

### 只指定輸入檔 （預設輸出檔為 output.pdf）
# python convert-md-pdf.py my-doc.md

### 指定輸入與輸出
# python convert-md-pdf.py my-doc.md report.pdf
