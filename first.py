from flask import Flask, request, jsonify
import requests
import gevent.monkey
gevent.monkey.patch_all()

app = Flask(_name_)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    unique_numbers = set()

    def fetch_numbers(url):
        try:
            response = requests.get(url, timeout=0.5)
            data = response.json().get('numbers', [])
            unique_numbers.update(data)
        except:
            pass

    threads = [gevent.spawn(fetch_numbers, url) for url in urls]
    gevent.joinall(threads)

    merged_numbers = sorted(list(unique_numbers))
    return jsonify(numbers=merged_numbers)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=3000)
