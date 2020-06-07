import json
from flask import Blueprint, request
from app.services.test import TestServices
from app.controllers import v1_test


@v1_test.route('/')
def home():
	return "Welcome to my test app"

@v1_test.route('/add', methods=['POST'])
def add():
	test_service = TestServices()
	data = json.loads(request.data.decode('utf-8'))
	print('[DATA RECEIVED] :: {}'.format(data))
	response = test_service.add_test(data.get('name'), data.get('age'))
	return response