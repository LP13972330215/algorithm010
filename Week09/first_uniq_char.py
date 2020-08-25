class Solution3(object):

    def firstUniqChar(self, s: str) -> int:
        dic = {}

        # 记录字符出现次数
        for c in s:
            dic[c] = dic[c] + 1 if c in dic else 1

        # 过滤出现次数不为一的字符
        unique_chars = [k for k, v in filter(lambda kvp: kvp[1] == 1, dic.items())]
        # 遍历目标字符串，返回首个出现在unique_chars中的字符的索引
        for i, c in enumerate(s):
            if c in unique_chars:
                return i

        return -1


if __name__ == "__main__":
    from flask import Flask, render_template, request
    from werkzeug import secure_filename
    import os

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'upload/'


    @app.route('/upload')
    def upload_file():
        return render_template('test.html')


    @app.route('/uploader', methods=['GET', 'POST'])
    def uploader():
        if request.method == 'POST':
            f = request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return 'file uploaded successfully'


    if __name__ == '__main__':
        app.run()