a = 'a'
b = 0

if __name__ == '__main__':
    try:
        print(b / a)
    except Exception as e:
        print(e)
        print(type(e).__name__)
    finally:
        print(a, b)
