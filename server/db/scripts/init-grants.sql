-- Grant root access from any host (needed for Docker cross-container access)
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- Fix account expiry dates
UPDATE newproject_db_auth.t_users SET a_end_date='2030-01-01 00:00:00' WHERE a_end_date < NOW();

-- Create default test account (user: test, password: test)
INSERT IGNORE INTO newproject_db_auth.bg_user (user_id, truepasswd, passwd, chk_service, partner_id, active_time, create_date)
VALUES ('test', 'test', '6bc2a95d1716c072495aed31a5afbfd97ffc02a7f4e32db5eb8bb49c116a4abd', 'Y', 'LC', NOW(), NOW());

SET @uid = LAST_INSERT_ID();

INSERT IGNORE INTO newproject_db_auth.t_users (a_idname, a_passwd, a_portal_index, a_end_date, a_enable)
VALUES ('test', '', @uid, '2030-01-01 00:00:00', 1);
