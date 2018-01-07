# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/yj_index', methods=('GET', ))
def yj_index():
    return jsonify({
        'code': 200,
        'msg': 'ok',
        'data': {
            'tbzhye': 81000,
            'mbzhye': 9000,
            'edzhye': 1000,
            'xjzhye': 2000,
            'cardNum': 3,
            'mbAdd': 10000,
            'mbTime': '08-10 22:00',
            'spAdd': 2000,
            'spTime': '08-11 10:00',
            'xjAdd': 30000,
            'xjTime': '08-12 12:00'
        }
    })


@app.route('/yj_transferAccounts', methods=('GET', ))
def yj_transferAccount():
    return jsonify(
        {
            'code': 200,
            'msg': 'ok',
            'data': {
                'tbzhye': 2000,
                'mbzhye': 3000,
                'xjzhye': 4000,
                'current_transfer_account': [
                    {
                        'id': 10001,
                        'from': {

                        },
                        'to': {
                            'userLogo': '../static/images/transferAccounts/user1.png',
                            'way': '支付宝',
                            'username': '杨娇',
                            'classify': '现金账户',
                            'use': '话费',
                            'money': 1000,
                            'time': '2017-12-24 11:00'
                        }
                    },
                    {
                        'id': 10002,
                        'from': {

                        },
                        'to': {
                            'userLogo': '../static/images/transferAccounts/user2.png',
                            'way': '现金',
                            'username': '卢鹏',
                            'classify': '现金账户',
                            'use': '圣诞礼物',
                            'money': 2000,
                            'time': '2017-12-24 12:00'
                        }
                    },
                    {
                        'id': 10003,
                        'from': {

                        },
                        'to': {
                            'userLogo': '../static/images/transferAccounts/user3.png',
                            'way': '白条',
                            'username': '杨娇',
                            'classify': '京东白条',
                            'use': '买烤鸭',
                            'money': 200,
                            'time': '2017-12-24 11:00'
                        }
                    },
                    {
                        'id': 10004,
                        'from': {

                        },
                        'to': {
                            'userLogo': '../static/images/transferAccounts/user4.png',
                            'way': '支付宝',
                            'username': '卢鹏',
                            'classify': '麦宝账户',
                            'use': '话费',
                            'money': 100,
                            'time': '2017-12-24 13:00'
                        }
                    }
                ]
            }
        }
    )


@app.route('/yj_transferAccount_nochoise', methods=('GET', 'POST'))
def yj_transferAccount_nochoice():
    if request.method == 'GET':
        return jsonify({
            'code': 200,
            'msg': 'ok',
            'data': {
                'account_username_input': '',
                'remain_money_input': 3000,
                'account_money_input': '',
                'remark_input': '',
                'verify_code_input': ''
            }
        })
    else:
        print(request.json)
        return jsonify({
            'code': 200,
            'msg': 'ok'
        })


@app.route('/yj_transferAccount_choise', methods=('GET', 'POST'))
def yj_transferAccount_choice():
    if request.method == 'GET':
        return jsonify({
            'code': 200,
            'msg': 'ok',
            'data': {
                'account_username_input': '',
                'account_person_input': '',
                'account_code_input': '',
                'remain_money_input': 3000,
                'account_money_input': '',
                'remark_input': '',
                'verify_code_input': ''
            }
        })
    else:
        print(request.json)
        return jsonify({
            'code': 200,
            'msg': 'ok'
        })


@app.route('/yj_accountList', methods=('GET', 'POST'))
def yj_accountList():
    if request.method == 'GET':
        return jsonify({
            'code': 200,
            'msg': 'ok',
            'data': {
                'current_transfer_account': [
                    {
                        'id': 10001,
                        'from': {

                        },
                        'to': {
                            'account_user': '../static/images/accountList/user_logo1.png',
                            'account_way': '支付宝',
                            'account_username': '杨娇',
                            'account_classify': '现金账户',
                            'account_datetime': '2017-12-24 11:00',
                            'account_money': 1000
                        }
                    },
                    {
                        'id': 10002,
                        'from': {

                        },
                        'to': {
                            'account_user': '../static/images/accountList/user_logo2.png',
                            'account_way': '现金',
                            'account_username': '卢鹏',
                            'account_classify': '现金账户',
                            'account_datetime': '2017-12-24 11:00',
                            'account_money': 2000
                        }
                    },
                    {
                        'id': 10003,
                        'from': {

                        },
                        'to': {
                            'account_user': '../static/images/accountList/user_logo3.png',
                            'account_way': '支付宝',
                            'account_username': '杨娇',
                            'account_classify': '现金账户',
                            'account_datetime': '2017-12-24 11:00',
                            'account_money': 4000
                        }
                    },
                    {
                        'id': 10004,
                        'from': {

                        },
                        'to': {
                            'account_user': '../static/images/accountList/user_logo4.png',
                            'account_way': '支付宝',
                            'account_username': 'LP',
                            'account_classify': '现金账户',
                            'account_datetime': '2017-12-24 11:00',
                            'account_money': 100
                        }
                    },
                    {
                        'id': 10005,
                        'from': {

                        },
                        'to': {
                            'account_user': '../static/images/accountList/user_logo5.png',
                            'account_way': '支付宝',
                            'account_username': 'YANGJIAO',
                            'account_classify': '现金账户',
                            'account_datetime': '2017-12-24 11:00',
                            'account_money': 400
                        }
                    },
                    {
                        'id': 10006,
                        'from': {

                        },
                        'to': {
                            'account_user': '../static/images/accountList/user_logo6.png',
                            'account_way': '支付宝',
                            'account_username': 'LIZE',
                            'account_classify': '现金账户',
                            'account_datetime': '2017-12-24 11:00',
                            'account_money': 800
                        }
                    },
                    {
                        'id': 10007,
                        'from': {

                        },
                        'to': {
                            'account_user': '../static/images/accountList/user_logo7.png',
                            'account_way': '支付宝',
                            'account_username': 'LP',
                            'account_classify': '现金账户',
                            'account_datetime': '2017-12-24 11:00',
                            'account_money': 1000
                        }
                    }
                ]
            }
        })


@app.route('/yj_header', methods=('GET', 'POST'))
def yj_header():
    return jsonify({
        'code': 200,
        'msg': 'ok',
        'data': {
            'backArrows_orange': '../static/images/header/backArrows.png'
        }
    })


if __name__ == '__main__':
    app.run()
