from flask import Flask, send_file, request
from image import open_image

import re

def is_hex(hex: str = "#23a9dd") -> str:
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex)

    if match:                      
        return hex
    
    return "#23a9dd"

# Start API server
app = Flask(__name__)

@app.route('/image', methods=['GET'])
def image_create():
    color = ""

    if not request.args.get('url'):
        return {'status': False, 'error': 'url not found'}

    if not request.args.get('text'):
        return {'status': False, 'error': 'text not found'}

    if 'color' in request.args:
        color = request.args.get('color')

    return send_file(
        open_image(
            url=request.args.get('url'), 
            text=request.args.get('text'),
            color=is_hex(color)
        ),
        mimetype='image/png',
        #download_name="custom_name.png",
        #as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)