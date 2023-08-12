from recipebook import db

class Category(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=False)
    recipe = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name




class Recipe(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(60), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    recipe_time = db.Column(db.Time, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)



    def __repr__(self):
        return f"#{self.id} - Recipe:{self.recipe_name} | Time: {self.recipe_time}"