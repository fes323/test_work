SELECT r.*
FROM room r
LEFT JOIN (
    SELECT placed_at_id, COUNT(*) AS total_chairs
    FROM chair
    WHERE type IN ('B', 'A')
    GROUP BY placed_at_id
) c ON r.id = c.placed_at_id
LEFT JOIN (
    SELECT placed_at_id, SUM(seats) AS total_seats
    FROM table
    GROUP BY placed_at_id
) t ON r.id = t.placed_at_id
WHERE COALESCE(t.total_seats, 0) < COALESCE(c.total_chairs, 0);
