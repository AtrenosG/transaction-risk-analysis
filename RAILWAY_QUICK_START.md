# 🚂 Railway Quick Start Guide

## 5-Minute Railway Deployment

### **Step 1: Push to GitHub** (2 minutes)
```bash
# In your project directory
git init
git add .
git commit -m "Initial commit"

# Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/transaction-risk-api.git
git push -u origin main
```

### **Step 2: Deploy to Railway** (2 minutes)
1. Go to [railway.app](https://railway.app)
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select your repository
4. Click **"Deploy Now"**

### **Step 3: Add Environment Variables** (1 minute)
In Railway dashboard → **Variables** tab:
```
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-supabase-anon-key
```

### **Step 4: Test Your API**
Your API will be live at: `https://your-project-name.up.railway.app`

Test endpoints:
- **Health**: `https://your-project-name.up.railway.app/api/health`
- **Docs**: `https://your-project-name.up.railway.app/docs`

---

## 🎯 **What You Get**

✅ **Production-Ready API** with automatic scaling  
✅ **SSL Certificate** included  
✅ **Health Monitoring** built-in  
✅ **Auto-Deploy** on git push  
✅ **Comprehensive Documentation** at `/docs`  
✅ **Error Handling** and logging  
✅ **CORS** configured for frontend integration  

---

## 📊 **API Endpoints**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/api/test` | GET | Simple test endpoint |
| `/api/health` | GET | Health check |
| `/api/analyze` | GET | Transaction analysis |
| `/api/results/{user_id}` | GET | Get user results |
| `/docs` | GET | Interactive API docs |

---

## 🔧 **Optional: Supabase Setup**

If you want full database functionality:

1. **Create Supabase Project**: [supabase.com](https://supabase.com)
2. **Run SQL** (in Supabase SQL Editor):
```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    account_no TEXT UNIQUE NOT NULL,
    ifsc_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Transactions table  
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    date TIMESTAMP NOT NULL,
    description TEXT,
    amount DECIMAL(15,2) NOT NULL,
    type TEXT CHECK (type IN ('credit', 'debit')),
    category TEXT,
    upi_app TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- ML Results table
CREATE TABLE ml_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    risk_score DECIMAL(5,2) NOT NULL,
    risk_category TEXT CHECK (risk_category IN ('low', 'medium', 'high')),
    eligible BOOLEAN NOT NULL,
    eligibility_reason TEXT,
    metrics JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

3. **Get Credentials**: Settings → API → Copy URL and anon key
4. **Add to Railway**: Variables tab

---

## 🚨 **Troubleshooting**

**Deployment Failed?**
- Check Railway logs in dashboard
- Verify all files are committed to git
- Ensure requirements.txt is correct

**API Not Responding?**
- Test `/api/test` endpoint first
- Check Railway application logs
- Verify environment variables

**Supabase Issues?**
- API works without Supabase
- Verify credentials in Railway variables
- Check Supabase project status

---

## 🎉 **You're Done!**

Your Transaction Risk Analytics API is now live and ready for production use!

**Next Steps:**
- Share your API URL with frontend team
- Set up monitoring alerts
- Configure custom domain (optional)

**Need Help?** Check `DEPLOYMENT_GUIDE.md` for detailed instructions.
