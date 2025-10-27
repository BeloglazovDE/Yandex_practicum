В этом проекте задачи выполняются на платформе. В этом файле будут собраны все этапы и их исполнения 

# Описание данных

![alt text](image.png)

## acquisition

Содержит информацию о покупках одних компаний другими.

Таблица включает такие поля:
* первичный ключ id — идентификатор или уникальный номер покупки;
* внешний ключ acquiring_company_id — ссылается на таблицу company — идентификатор компании-покупателя, то есть той, что покупает другую компанию;
* внешний ключ acquired_company_id — ссылается на таблицу company — идентификатор компании, которую покупают;
* term_code — способ оплаты сделки:
  * cash — наличными;
  * stock — акциями компании;
  * cash_and_stock — смешанный тип оплаты: наличные и акции.
* price_amount — сумма покупки в долларах;
* acquired_at — дата совершения сделки;
* created_at — дата и время создания записи в таблице;
* updated_at — дата и время обновления записи в таблице.
## company
Содержит информацию о компаниях-стартапах.
* первичный ключ id — идентификатор, или уникальный номер компании;
* name — название компании;
* category_code — категория деятельности компании, например:
  * news — специализируется на работе с новостями;
  * social — специализируется на социальной работе.
* status — статус компании:
  * acquired — приобретена;
  * operating — действует;
  * ipo — вышла на IPO;
  * closed — перестала существовать.
* founded_at — дата основания компании;
* closed_at — дата закрытия компании, которую указывают в том случае, если компании больше не существует;
* domain — домен сайта компании;
* network_username — профиль фонда в корпоративной сети биржи;
* country_code — код страны, например, USA для США, GBR для Великобритании;
* investment_rounds — число раундов, в которых компания участвовала как инвестор;
* funding_rounds — число раундов, в которых компания привлекала инвестиции;
* funding_total — сумма привлечённых инвестиций в долларах;
* milestones — количество важных этапов в истории компании;
* created_at — дата и время создания записи в таблице;
* updated_at — дата и время обновления записи в таблице.
## education
Хранит информацию об уровне образования сотрудников компаний.
* первичный ключ id — уникальный номер записи с информацией об образовании;
* внешний ключ person_id — ссылается на таблицу people — идентификатор человека, информация о котором представлена в записи;
* degree_type — учебная степень, например:
  * BA — Bachelor of Arts — бакалавр гуманитарных наук;
  * MS — Master of Science — магистр естественных наук.
* instituition — учебное заведение, название университета;
* graduated_at — дата завершения обучения, выпуска;
* created_at — дата и время создания записи в таблице;
* updated_at — дата и время обновления записи в таблице.
## fund
Хранит информацию о венчурных фондах. 
* первичный ключ id — уникальный номер венчурного фонда;
* name — название венчурного фонда;
* founded_at — дата основания фонда;
* domain — домен сайта фонда;
* network_username — профиль фонда в корпоративной сети биржи;
* country_code — код страны фонда;
* investment_rounds — число инвестиционных раундов, в которых фонд принимал участие;
* invested_companies — число компаний, в которые инвестировал фонд;
* milestones — количество важных этапов в истории фонда;
* created_at — дата и время создания записи в таблице;
* updated_at — дата и время обновления записи в таблице.
## funding_round
Содержит информацию о раундах инвестиций. 
* первичный ключ id — уникальный номер инвестиционного раунда;
* внешний ключ company_id — ссылается на таблицу company — уникальный номер компании, участвовавшей в инвестиционном раунде;
* funded_at — дата проведения раунда;
* funding_round_type — тип инвестиционного раунда, например:
  * venture — венчурный раунд;
  * angel — ангельский раунд;
  * series_a — раунд А.
* raised_amount — сумма инвестиций, которую привлекла компания в этом раунде в долларах;
* pre_money_valuation — предварительная, проведённая до инвестиций оценка стоимости компании в долларах;
* participants — количество участников инвестиционного раунда;
* is_first_round — является ли этот раунд первым для компании;
* is_last_round — является ли этот раунд последним для компании;
* created_at — дата и время создания записи в таблице;
* updated_at — дата и время обновления записи в таблице.
## investment
Содержит информацию об инвестициях венчурных фондов в компании-стартапы.
* первичный ключ id — уникальный номер инвестиции;
* внешний ключ funding_round_id — ссылается на таблицу funding_round — уникальный номер раунда инвестиции;
* внешний ключ company_id — ссылается на таблицу company — уникальный номер компании-стартапа, в которую инвестируют;
* внешний ключ fund_id — ссылается на таблицу fund — уникальный номер фонда, инвестирующего в компанию-стартап;
* created_at — дата и время создания записи в таблице;
* updated_at — дата и время обновления записи в таблице.
## people
Содержит информацию о сотрудниках компаний-стартапов.
* первичный ключ id — уникальный номер сотрудника;
* first_name — имя сотрудника;
* last_name — фамилия сотрудника;
* внешний ключ company_id — ссылается на таблицу company — уникальный номер компании-стартапа;
* network_username — профиль фонда в корпоративной сети биржи;
* created_at — дата и время создания записи в таблице;
* updated_at — дата и время обновления записи в таблице.

# Выполнение заданий

Простые задачи здесь будут пропущены. Остановимся на чуть более интересных запросах

## Анализ фондов разных стран

> Задача: Проанализируйте, в каких странах находятся фонды, которые чаще всего инвестируют в стартапы. 
> Для каждой страны посчитайте минимальное, максимальное и среднее число компаний, в которые инвестировали фонды этой страны, основанные с 2010 по 2012 год включительно. Исключите страны с фондами, у которых минимальное число компаний, получивших инвестиции, равно нулю. 
> Выгрузите десять самых активных стран-инвесторов: отсортируйте таблицу по среднему количеству компаний от большего к меньшему. Затем добавьте сортировку по коду страны в лексикографическом порядке.

```SQL
SELECT country_code AS country,
    MIN(invested_companies) AS min_comp_amount,
    MAX(invested_companies) AS max_comp_amount,
    AVG(invested_companies) AS avg_comp_amount
FROM fund
WHERE EXTRACT(YEARS FROM founded_at) BETWEEN 2010 AND 2012
GROUP BY country
HAVING MIN(invested_companies) > 0
ORDER BY avg_comp_amount DESC
LIMIT 10;
```

## Отбор сотрудников закрытых компаний с единственным раундом

> Задача: Составьте список уникальных номеров сотрудников, работавыших в закрытых компаниях, прошедших единственный раунд финансирования

```SQL
WITH 
    closed_single_round_comp AS (
        SELECT DISTINCT c.name,
            c.id
        FROM company AS c
        INNER JOIN funding_round AS fr ON fr.company_id = c.id
        WHERE status = 'closed'
            AND is_first_round = 1
            AND is_last_round = 1
    )

SELECT DISTINCT p.id
FROM people AS p
INNER JOIN closed_single_round_comp AS csrc ON p.company_id = csrc.id;
```

## Анализ образования сотрудников из компаний с единственным раундом

> Задача: Проанализировать уровень образования сотрудников стартапов, которые завершили свою деятельность, пройдя всего один раунд финансирования. Найти всех людей, которые работали в таких компаниях. Для каждого такого человека посчитать количество учебных заведений, которые он окончил (указал в своем профиле). Результат отсортировать по убыванию количества образовательных программ, чтобы увидеть самых "образованных" сотрудников неудавшихся стартапов.

```SQL
WITH closed_companies AS (
    SELECT DISTINCT c.id
    FROM company AS c
    INNER JOIN funding_round fr ON fr.company_id = c.id
    WHERE c.status = 'closed'
      AND fr.is_first_round = 1
      AND fr.is_last_round = 1
)

SELECT p.id AS person_id,
       COUNT(e.instituition) AS education_count
FROM people AS p
JOIN closed_companies AS cc ON p.company_id = cc.id
JOIN education e ON e.person_id = p.id
GROUP BY p.id
ORDER BY education_count DESC;
```

## Анализ покупок компаний

> Задача: Выгрузите таблицу, в которой будут такие поля:
> название компании-покупателя;
> сумма сделки;
> название компании, которую купили;
> сумма инвестиций, вложенных в купленную компанию;
> доля, которая отображает, во сколько раз сумма покупки превысила сумму вложенных в компанию инвестиций, округлённая до ближайшего целого числа.
> Не учитывайте те сделки, в которых сумма покупки равна нулю. Если сумма инвестиций в компанию равна нулю, исключите такую компанию из таблицы. 
> Отсортируйте таблицу по сумме сделки от большей к меньшей, а затем по названию купленной компании в лексикографическом порядке. Ограничьте таблицу первыми десятью записями.

```SQL
SELECT 
    acq_c.name AS acquiring_company_name,
    a.price_amount AS deal_amount,
    acd_c.name AS acquired_company_name,
    acd_c.funding_total AS total_investment_in_acquired,
    ROUND(a.price_amount / acd_c.funding_total) AS investment_ratio
FROM acquisition a
INNER JOIN company AS acq_c ON acq_c.id = a.acquiring_company_id
INNER JOIN company AS acd_c ON acd_c.id = a.acquired_company_id
WHERE a.price_amount > 0 AND acd_c.funding_total > 0
ORDER BY a.price_amount DESC, 
    acd_c.name
LIMIT 10;
```

## Анализ месяцев за 4 года

> Отберите данные по месяцам с 2010 по 2013 год, когда проходили инвестиционные раунды. Сгруппируйте данные по номеру месяца и получите таблицу, в которой будут поля:
> номер месяца, в котором проходили раунды;
> количество уникальных названий фондов из США, которые инвестировали в этом месяце;
> количество компаний, купленных за этот месяц;
> общая сумма сделок по покупкам в этом месяце.

```SQL
WITH
    unique_fund_amount AS (
        SELECT 
            EXTRACT(MONTH FROM fr.funded_at) AS month_num,
            COUNT(DISTINCT f.name) AS fund_amount
        FROM funding_round AS fr
        INNER JOIN investment AS i ON i.funding_round_id = fr.id
        INNER JOIN fund AS f ON f.id = i.fund_id 
        WHERE f.country_code = 'USA'
            AND EXTRACT(YEAR FROM fr.funded_at) BETWEEN 2010 AND 2013
        GROUP BY EXTRACT(MONTH FROM fr.funded_at)
    ),
    acquired_company_amount_and_sum AS (
        SELECT 
            EXTRACT(MONTH FROM a.acquired_at) AS month_num,
            COUNT(a.acquired_company_id) AS company_amount,
            SUM(a.price_amount) AS total_price
        FROM acquisition AS a
        WHERE EXTRACT(YEAR FROM a.acquired_at) BETWEEN 2010 AND 2013
        GROUP BY EXTRACT(MONTH FROM a.acquired_at)
    )

SELECT 
    ufa.month_num,
    ufa.fund_amount,
    COALESCE(acas.company_amount, 0) AS company_amount,
    COALESCE(acas.total_price, 0) AS total_price
FROM unique_fund_amount AS ufa
LEFT JOIN acquired_company_amount_and_sum AS acas ON acas.month_num = ufa.month_num
ORDER BY ufa.month_num;
```