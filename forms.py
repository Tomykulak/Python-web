from wtforms import Form, StringField, validators, PasswordField, SelectField, IntegerField
from wtforms.validators import NumberRange

class Sign_in_form(Form):
    login = StringField(name='login', label='Login',
                        validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    password = PasswordField(name='password', label='Password',
                             validators=[validators.Length(min=3), validators.InputRequired()])

class Edit_profile_form(Form):
    new_first_name = StringField(name='new_first_name', label='New First Name',
                                 validators=[validators.Length(min=0, max=30)])
    new_email = StringField(name='new_email', label='new email',
                            validators=[validators.Length(min=0, max=30)])

    new_password = PasswordField(name='new_password', label='new password',
                                 validators=[validators.Length(min=0)])


class Add_profile(Form):
    new_position = SelectField(name = 'new_position', label='Position', choices=[('Admin','Admin'),('Employee', 'Employee'), ('Customer', 'Customer')], 
                            validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    new_first_name = StringField(name='new_first_name', label='First Name',
                            validators=[validators.Length(min=2, max=30), validators.InputRequired()])
    new_last_name = StringField(name='new_last_name', label='Last Name',
                            validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    new_phone_number = StringField(name='new_phone_number', label='Phone Number',
                            validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    new_email = StringField(name='new_email', label='Email',
                            validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    new_hourly_wage = IntegerField(name='new_hourly_wage', label='Hourly Wage', 
                            validators=[NumberRange(min=0, max=10000), validators.InputRequired()])
    
    new_login_name = StringField(name='new_login_name', label='Login Name',
                            validators=[validators.Length(min=2, max=30), validators.InputRequired()])


    new_password = PasswordField(name='new_password', label='New Password',
                            validators=[validators.Length(min=2, max=30), validators.InputRequired()])

    new_company_id = SelectField(name = 'new_company_id', label='Company ID', choices=[(1, 'FajnovaFirma')], 
                            validators=[validators.InputRequired()])

    new_active = SelectField(name = 'new_active', label='Activate Account', choices=[(0, 'Innactive'), (1, 'Active')], 
                            validators=[validators.InputRequired()])


class Add_phone(Form):
    new_img = StringField(name='new_img', label='Image',
                                 validators=[validators.Length(min=0, max=30), validators.InputRequired()])

    new_workload = IntegerField(name='new_workload', label='Workload',
                                 validators=[NumberRange(min=0, max=30), validators.InputRequired()])
    new_type = SelectField(name = 'new_type', label='Type', choices=[('smartphone', 'Smart-phone'), ('featurephone', 'Feature-phone')], 
                            validators=[validators.InputRequired()])

    new_name = StringField(name='new_name', label='Name',
                                 validators=[validators.Length(min=0), validators.InputRequired()])