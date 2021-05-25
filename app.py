"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify,render_template
from models import db, connect_db,Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def all_cupcakes():
    cakes = Cupcake.query.all()
    return render_template('index.html',cakes=cakes)


# Restfull

@app.route('/api/cupcakes')
def list_cupcakes():
    cupcakes = [cakes.serialize_cupcake()  for cakes in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake.serialize_cupcake())

@app.route('/api/cupcakes',methods=["POST"])
def create_cupcake():
    newCupcake = Cupcake(flavor=request.json["flavor"],
                        size=request.json["size"],
                        rating=request.json["rating"],
                        image=request.json.get('image','https://tinyurl.com/demo-cupcake'))

    db.session.add(newCupcake)
    db.session.commit()
    response_json = jsonify(cupcake=newCupcake.serialize_cupcake())
    return (response_json,201)

@app.route('/api/cupcakes/<int:id>',methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get('size',cupcake.size)
    cupcake.rating = request.json.get('rating',cupcake.rating)
    cupcake.image = request.json.get('image',cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize_cupcake())


@app.route('/api/cupcakes/<int:id>',methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Cupcake Deleted")