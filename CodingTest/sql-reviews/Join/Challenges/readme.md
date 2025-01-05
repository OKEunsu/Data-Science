SELECT h.hacker_id, h.name, COUNT(*) cnt
FROM hackers h
     INNER JOIN challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING cnt = (SELECT max(sub.cnt) as maxcnt
                FROM (
                    SELECT hacker_id, count(*) as cnt
                    FROM challenges
                    GROUP BY hacker_id
                ) sub)
OR cnt IN (SELECT sub.cnt
                FROM (
                    select hacker_id, count(*) as cnt
                    from challenges
                    group by hacker_id
                ) sub
                GROUP BY sub.cnt
                HAVING count(*) = 1)
ORDER BY cnt DESC, h.hacker_id
