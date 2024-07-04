from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/clothing')
def clothing():
    clothing = ['Футболка', 'Джинсы', 'Платье']
    return render_template('clothing.html', clothing=clothing)

@app.route('/shoes')
def shoes():
    shoes = ['Кроссовки', 'Туфли', 'Ботинки']
    return render_template('shoes.html', shoes=shoes)



if __name__ == '__main__':
    app.run(debug=True)