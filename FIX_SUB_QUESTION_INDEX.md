# Fix for Sub-Question Index Error

## Problem
The deployed application was crashing when trying to submit exercise responses with the error:
```
psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type integer: "section_0_question_0"
```

This occurred because:
- The new exercise format uses string identifiers like `"section_0_question_0"` for sub-questions
- The database column `sub_question_index` was defined as `INTEGER`
- PostgreSQL rejected the string values

## Solution
Changed the `sub_question_index` column from `INTEGER` to `TEXT` to support both:
- Legacy format: integer indices (0, 1, 2, ...) stored as strings ("0", "1", "2")
- New format: section identifiers ("section_0_question_0", "section_1_question_2", etc.)

## Files Changed
1. **backend/models.py** - Updated column type from `Integer` to `String`
2. **backend/routes/modules.py** - Normalize sub_question_index to string before storage
3. **backend/routes/auth.py** - Updated to handle string representations of integers
4. **backend/migrate_sub_question_index_to_text.py** - Migration script (new file)

## Deployment Steps for Railway

### Step 1: Push code changes to GitHub
```bash
git add backend/models.py backend/routes/modules.py backend/routes/auth.py backend/migrate_sub_question_index_to_text.py FIX_SUB_QUESTION_INDEX.md
git commit -m "Fix sub_question_index type mismatch - change to TEXT to support new exercise format"
git push origin main
```

### Step 2: Run migration on Railway

1. Go to your Railway project dashboard
2. Click on your backend service
3. Go to the **"Settings"** tab
4. Find **"Environment Variables"** - make sure `DATABASE_URL` is set
5. Go back to **"Deployments"** tab
6. Wait for the new deployment to finish (this will deploy the updated code)
7. Once deployed, click on the deployment
8. Click on **"View Logs"** to monitor
9. Open **"Shell"** (or use Railway CLI)
10. Run the migration:

```bash
python backend/migrate_sub_question_index_to_text.py
```

### Step 3: Verify the fix
After the migration completes successfully, test by:
1. Opening your deployed application
2. Navigating to any exercise with the new format
3. Submitting a response
4. Confirm no more `InvalidTextRepresentation` errors

## Alternative: Using Railway CLI

If you have Railway CLI installed:

```bash
# Login to Railway
railway login

# Link to your project
railway link

# Run the migration
railway run python backend/migrate_sub_question_index_to_text.py
```

## What the Migration Does

1. ✅ Checks current column type (INTEGER)
2. ✅ Creates a backup table with existing data
3. ✅ Alters column type from INTEGER to TEXT
4. ✅ Converts existing integer values to text format
5. ✅ Verifies data integrity
6. ✅ Cleans up backup table

## Backward Compatibility

The code now handles all three cases:
- **Integer values** (old code might still pass these): Converted to string
- **String integers** ("0", "1", "2"): Legacy format after migration
- **Section identifiers** ("section_0_question_0"): New exercise format

All existing data is preserved and will continue to work.

## Rollback (if needed)

If something goes wrong, the migration script creates a backup table. However, since we're only changing the column type and not the data structure, rollback would require:

1. Restore from Railway database backup (if available)
2. Or manually revert the column type (only if no new section-format responses were submitted)

⚠️ **Note**: Once users start submitting responses in the new format ("section_X_question_Y"), you cannot roll back to INTEGER type without data loss.

## Testing the Fix Locally

Before deploying, you can test locally with your local database:

```bash
# Make sure you're using PostgreSQL locally (not SQLite)
# Or temporarily modify the script for SQLite

python backend/migrate_sub_question_index_to_text.py
```

Then test submitting responses through your local frontend.

