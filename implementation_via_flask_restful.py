#
## В данном файле представлена рабочая реализация приложения REST API через flask_restful (проверена через postman)
#
# import json
# from collections import OrderedDict
#
# from flask_restful import Resource, Api
# from flask import Flask, request
#
# from calculation_deposit import calculation_deposit
#
# app = Flask(__name__)
# api = Api(app)
#
# deposit_details = {}
#
#
# class ResultCalculationDeposit(Resource):
#     def post(self):
#         initial_deposit = request.get_json()
#
#         deposit_details['date'] = initial_deposit['date']
#         deposit_details['periods'] = initial_deposit['periods']
#         deposit_details['amount'] = initial_deposit['amount']
#         deposit_details['rate'] = initial_deposit['rate']
#
#         try:
#             new = OrderedDict(calculation_deposit(deposit_details))
#         except:
#             return json.dumps({'ValueError': calculation_deposit(deposit_details)}), 400, \
#                    print({'ValueError': calculation_deposit(deposit_details)})
#
#         try:
#             new = json.dumps(new)
#             return new, 200, print(new)
#         except Exception as e:
#             return json.dumps({'error': str(e)}), 400
#
#
# api.add_resource(ResultCalculationDeposit, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)
