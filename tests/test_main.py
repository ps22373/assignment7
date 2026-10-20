import main


def test_valid_url():
    assert main.is_valid_url("https://www.njit.edu") is True


def test_invalid_url():
    assert main.is_valid_url("not-a-url") is False


def test_create_directory(tmp_path):
    directory = tmp_path / "nested" / "qr_codes"

    main.create_directory(directory)

    assert directory.is_dir()


def test_generate_qr_code_success(tmp_path):
    output = tmp_path / "test_qr.png"

    main.generate_qr_code(
        "https://www.njit.edu",
        output,
        "red",
        "white",
    )

    assert output.exists()
    assert output.stat().st_size > 0


def test_generate_qr_code_invalid_url(tmp_path):
    output = tmp_path / "invalid_qr.png"

    main.generate_qr_code(
        "not-a-url",
        output,
        "red",
        "white",
    )

    assert not output.exists()