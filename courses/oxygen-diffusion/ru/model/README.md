# Verified oxygen model

Python 3.9 or later, standard library only. From the language directory run `python3 model/oxygen_model.py --out my-run` with a fresh output directory. Without Python, inspect the archived profiles and verification report.

Укажите новый каталог или уже существующий пустой каталог. Непустой каталог отклоняется до вычислений и записи; его содержимое сохраняется. В текущий код добавлена только эта проверка каталога, а идентификатор кода выполненного расчёта и исходные результаты сохранены как исторические в `../provenance.json`. Команды в архивном отчёте описывают исходный запуск; для текущей команды выберите новый каталог вывода.

`model-contract.md` defines units, assumptions and boundaries. `verification-report.md` and `results/verification.json` document analytical, conservation, convergence and synthetic-fit checks. All parameters and fitting observations are illustrative. Numerical verification does not establish field validity. The separate optional measured-data exercise is in `../../optional-observed-data/`.
