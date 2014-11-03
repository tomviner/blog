Title: Py.Test Fixtures
Tags: python, testing, pytest
Date: 2014-8-23


##### Based on [Advanced py.test Fixtures](http://devork.be/talks/advanced-fixtures/advfix.html)
by Floris Bruynooghe

## Basic example

Fixtures are a method of dependancy injection

    @pytest.fixture
    def smtp():
        import smtplib
        return smtplib.SMTP("merlinux.eu")

# Scope

Allows cachine of fixture over session/module/function (default)

    @pytest.fixture(scope='session')
    def db_conn():
        ...
        return conn

# Combine fixtures

    @pytest.fixture(scope='function')
    def db_row(db_conn):
        return db_conn.get_row()

# Skip / Fail

# Mark

# Mark with args

# Parameterised

# Plugins


