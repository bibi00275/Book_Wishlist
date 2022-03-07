from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
import sqlite3

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer)
    isbn = db.Column(db.Text)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)


class Wishlist(db.Model):
    __tablename__ = 'wishlist'

    id = db.Column(db.Integer, primary_key=True,)
    isbn = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    date_of_publication = db.Column(db.Text)
    title = db.Column(db.Text)

def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn



class wishlist(Resource):
    def get(self):
        rows = Wishlist.query.all()
        result = []
        # Convert to serialized format for display
        for row in rows:
            result.append({
                        'id': row.id,
                        'isbn':row.isbn,
                         'user_id': row.user_id,
                         'date_of_publication': row.date_of_publication,
                         'title': row.title})
        print(result)
        return jsonify({'wishlist': result})

    def post(self):
        try:
            isbn = request.values['isbn']
        except:
            return jsonify({'error': 'Please provide a isbn'})
        try:
            user_id = request.values['user_id']
        except:
            return jsonify({'error': 'Please provide a user_id'})
        try:
            pubdate = request.values['date_of_publication']
        except:
            return jsonify({'error': 'Please provide a date_of_publication'})
        try:
            title = request.values['title']
        except:
            return jsonify({'error': 'Please provide a title'})

        newwishlist = Wishlist(
            isbn=isbn,
            user_id=user_id,
            date_of_publication=pubdate,
            title=title
        )
        db.session.add(newwishlist)
        db.session.commit()
        return jsonify({'success': 'Your book has been added to wishlist'})


class updatewishlist(Resource):
    def post(self):

        try:
            wid = request.values['id']
            obj = db.session.query(Wishlist).get(int(wid))
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)})
        try:
            isbn = request.values['isbn']
            obj.isbn = isbn

        except:
            isbn = None
        try:
            user_id = request.values['user_id']
            obj.user_id = user_id
        except:
            user_id = None
        try:
            pubdate = request.values['date_of_publication']
            obj.date_of_publication = pubdate
        except:
            pubdate = None
        try:
            title = request.values['title']
            obj.title = title
        except:
            title = None
        
        db.session.flush()
        db.session.commit()

        return jsonify({'success': f'wishlist item {wid} has been updated'})

class deletewishlist(Resource):
    def post(self):
        try:
            wid = request.values['id']
        except:
            return jsonify({'error': 'Please provide the id of the wishlist item to delete'})

        Wishlist.query.filter_by(id=int(wid)).delete()
        db.session.commit()

        return jsonify({'success': f'wishlist item {wid} has been deleted'})


api.add_resource(wishlist, '/wishlist')
api.add_resource(updatewishlist, '/updatewishlist')
api.add_resource(deletewishlist, '/deletewishlist')




if __name__ == '__main__':
    app.run(debug=True)
