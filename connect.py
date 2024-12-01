from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db", echo=True) # set optional argument echo=True to get logs

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))

    print(result.all())