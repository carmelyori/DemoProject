def test_hello_world(capsys):
    import hello_world
    captured = capsys.readouterr
    assert captured.out == "Hello World\n\"
