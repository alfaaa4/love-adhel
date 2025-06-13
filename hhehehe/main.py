from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rahasia_super_love'

# Dummy user
KAMU_SAYANG_AKU_GA = 'sayang'
TANGGAL_JADIAN = '8 januari'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['kamu_sayang_aku_ga']
        pw = request.form['tanggal_jadian']
        if user == KAMU_SAYANG_AKU_GA and pw == TANGGAL_JADIAN:
            session['user'] = user
            return redirect(url_for('love'))
        else:
            return render_template('login.html', error='salahh ih kamu gimana sii')
    return render_template('login.html')

@app.route('/love')
def love():
    if 'user' in session:
        return render_template('love.html')
    return redirect(url_for('login'))

@app.route('/love-letter')
def love_letter():
    if 'user' in session:
        return render_template('love_letter.html')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
