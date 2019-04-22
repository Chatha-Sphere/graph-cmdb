from flask_wtf import FlaskForm
from wtforms import Form, IntegerField, StringField, SubmitField, validators


#do i need an id_ field? or can the ORM generate automatically
class AssetForm(FlaskForm):
    id_ = IntegerField("ID", [validators.InputRequired()])
    name = StringField("Name", [validators.InputRequired()])
    type_ = StringField("Type")
    loc = StringField("Location")
    desc = StringField("Description")
    access = StringField("Access Rights")
    admin = StringField("Administrator")
    url = StringField("URL")
    submit = SubmitField("Add Asset")

class HardwareForm(FlaskForm):
    id_ = IntegerField("ID", [validators.InputRequired()])
    serial_number = StringField("Serial Number")
    type_ = StringField("Type") 
    loc = StringField("Location")
    assigned_to = StringField("Assignee")
    admin_pw = StringField("Admin Password")
    status = StringField("Status")
    name = StringField("Name")
    submit = SubmitField("Add Hardware Item")

class DependencyForm(FlaskForm):
    #child depends on parent with dependency type
    child_id = IntegerField("Child ID", [validators.InputRequired()])
    parent_id = IntegerField("Parent ID", [validators.InputRequired()])
    type_ = StringField("Dependency Type", [validators.InputRequired()])
    submit = SubmitField("Add Dependency")