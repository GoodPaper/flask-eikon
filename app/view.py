from app import webapp


@webapp.route( '/' )
def index():
    
    return 'FLASK-EIKON is running.'
