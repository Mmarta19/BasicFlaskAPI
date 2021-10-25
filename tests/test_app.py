# Test for the endpoint /password_check
import app


def test_password_check():
    _app = app.create_app()
    with _app.test_client() as c:
        # Test with a integer instead of string
        rv = c.get('/password_check', json={'password': 42})
        assert not rv.get_json(force=True)['response']

        # Test less than 10 digits
        rv = c.get('/password_check', json={'password': 'ABCabc42'})
        assert not rv.get_json(force=True)['response']

        # Test with more than 10 digits
        rv = c.get('/password_check', json={'password': 'ABCabcABC42'})
        assert not rv.get_json(force=True)['response']

        # Test without uppercase
        rv = c.get('/password_check', json={'password': 'abcabcab42'})
        assert not rv.get_json(force=True)['response']

        # Test without numbers
        rv = c.get('/password_check', json={'password': 'abcABCabcA'})
        assert not rv.get_json(force=True)['response']

        # Test with correct password
        rv = c.get('/password_check', json={'password': 'ABCabcABC4'})
        assert rv.get_json(force=True)['response']
