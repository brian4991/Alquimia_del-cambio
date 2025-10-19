-- Simple SQL migration to change sub_question_index from INTEGER to TEXT
-- Run this directly in Railway PostgreSQL console

BEGIN;

-- Backup existing data (optional, for safety)
CREATE TABLE user_sub_question_responses_backup AS 
SELECT * FROM user_sub_question_responses;

-- Alter column type from INTEGER to TEXT
ALTER TABLE user_sub_question_responses 
ALTER COLUMN sub_question_index TYPE TEXT 
USING sub_question_index::TEXT;

-- Verify the change
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'user_sub_question_responses' 
AND column_name = 'sub_question_index';

-- If everything looks good, commit
COMMIT;

-- After verification, you can drop the backup:
-- DROP TABLE user_sub_question_responses_backup;

