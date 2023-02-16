-- Lists all the cities of CA in the db
-- Results are ordered in ASC order
SELECT `id`, `name` FROM `cities` WHERE `state_id` IN (SELECT `id` FROM `states` WHERE `name` = "California")
ORDER BY `id`;
