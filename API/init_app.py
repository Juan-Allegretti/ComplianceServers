from app import create_app
#from app.utils.db import DBcon


app = create_app()

if __name__ == "__main__":  # only in dev	
	#conn = DBcon().get_con()
	app.run(host="0.0.0.0", port=8080, debug=True)