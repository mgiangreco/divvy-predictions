#!venv/bin/python2.7

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_restful.utils import cors
import requests
from predictor import Predictor

app = Flask(__name__, static_url_path="")
api = Api(app, decorators=[cors.crossdomain(origin="*")])
predictor = Predictor()



class ForecastAPI(Resource):

	def get(self):
		return { 'forecast': requests.get('https://api.forecast.io/forecast/53b2466f3793d7f9f048831394011b21/41.88917683,-87.63850577').content }



class PredictionsAPI(Resource):

	def get(self):
		print predictor.get_predictions()
		return { 'predictions': predictor.get_predictions() }



api.add_resource(ForecastAPI, '/divvyPredictions/api/v1.0/forecast', endpoint='forecast')
api.add_resource(PredictionsAPI, '/divvyPredictions/api/v1.0/predictions', endpoint='predictions')



if __name__ == "__main__":
	app.run(debug=True)