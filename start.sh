uvicorn main:app --app-dir backend/src --reload &
cd frontend/src
npm run dev &
cd ../..
caddy run
sleep infinity
