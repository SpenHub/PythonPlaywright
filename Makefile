install:
    source ./venv/bin/activate; \
    pip install -r requirements.txt; \
    echo "do other stuff after in the same environment"

test:
    python -m unittest discover -v


# and so on, you got the idea
