-- Migration script for adding exercise sections and questions fields
-- Run this SQL directly on the PostgreSQL database

-- Add exercise_instructions column if it doesn't exist
DO $$ 
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'exercises' AND column_name = 'exercise_instructions'
    ) THEN
        ALTER TABLE exercises ADD COLUMN exercise_instructions TEXT;
        RAISE NOTICE 'Added exercise_instructions column';
    ELSE
        RAISE NOTICE 'exercise_instructions column already exists';
    END IF;
END $$;

-- Add exercise_questions column if it doesn't exist
DO $$ 
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'exercises' AND column_name = 'exercise_questions'
    ) THEN
        ALTER TABLE exercises ADD COLUMN exercise_questions TEXT DEFAULT '[]';
        RAISE NOTICE 'Added exercise_questions column';
    ELSE
        RAISE NOTICE 'exercise_questions column already exists';
    END IF;
END $$;

-- Add exercise_sections column if it doesn't exist
DO $$ 
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'exercises' AND column_name = 'exercise_sections'
    ) THEN
        ALTER TABLE exercises ADD COLUMN exercise_sections TEXT DEFAULT '[]';
        RAISE NOTICE 'Added exercise_sections column';
    ELSE
        RAISE NOTICE 'exercise_sections column already exists';
    END IF;
END $$;

-- Add created_at column if it doesn't exist
DO $$ 
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'exercises' AND column_name = 'created_at'
    ) THEN
        ALTER TABLE exercises ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
        RAISE NOTICE 'Added created_at column';
    ELSE
        RAISE NOTICE 'created_at column already exists';
    END IF;
END $$;

-- Add updated_at column if it doesn't exist
DO $$ 
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'exercises' AND column_name = 'updated_at'
    ) THEN
        ALTER TABLE exercises ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
        RAISE NOTICE 'Added updated_at column';
    ELSE
        RAISE NOTICE 'updated_at column already exists';
    END IF;
END $$;

-- Verify the migration
SELECT 
    column_name, 
    data_type, 
    column_default,
    is_nullable
FROM information_schema.columns 
WHERE table_name = 'exercises' 
ORDER BY ordinal_position;
