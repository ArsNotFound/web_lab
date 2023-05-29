from flask import render_template

from app.error import bp


@bp.route('/404')
def not_found_html():
    return render_template('404.html', title='404', err={'error': 'Not found', 'code': 404}), 404
