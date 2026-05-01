def calculate_device_risk_score(device_data):
    """
    Calculate device risk score based on device data.
    
    Args:
        device_data (dict): Device data containing 'ip_address', 'user_agent', 'location', 'browser_type', 'os_type', 'device_type'
    
    Returns:
        int: Device risk score (0-100)
    """
    
    # Belgilangan xususiyatlarning vazifasi haqida ma'lumot beruvchi lug'at
    risk_factors = {
        'ip_address': 10,
        'user_agent': 20,
        'location': 15,
        'browser_type': 10,
        'os_type': 15,
        'device_type': 30
    }
    
    # Belgilangan xususiyatlarning qiymatlarini olish
    ip_address = device_data.get('ip_address', 0)
    user_agent = device_data.get('user_agent', 0)
    location = device_data.get('location', 0)
    browser_type = device_data.get('browser_type', 0)
    os_type = device_data.get('os_type', 0)
    device_type = device_data.get('device_type', 0)
    
    # Xususiyatlarning qiymatlarini o'rganib, risk ballini hisoblash
    risk_score = (ip_address * risk_factors['ip_address'] + 
                  user_agent * risk_factors['user_agent'] + 
                  location * risk_factors['location'] + 
                  browser_type * risk_factors['browser_type'] + 
                  os_type * risk_factors['os_type'] + 
                  device_type * risk_factors['device_type'])
    
    # Risk ballini 0 dan 100 gacha qayta hisoblash
    risk_score = int((risk_score / sum(risk_factors.values())) * 100)
    
    return risk_score
```

Kodni ishlatish uchun misol:
```python
device_data = {
    'ip_address': '192.168.1.1',
    'user_agent': 'Mozilla/5.0',
    'location': 'New York',
    'browser_type': 'Chrome',
    'os_type': 'Windows',
    'device_type': 'Desktop'
}

risk_score = calculate_device_risk_score(device_data)
print(risk_score)
