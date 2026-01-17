```python
#!/usr/bin/env python3
"""
快速验证DID模块功能
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("🧪 Xiongan Civilization OS - 快速验证")
print("=" * 50)

try:
    # 尝试导入
    from src.core.did import DID
    
    print("✅ 模块导入成功")
    
    # 快速测试
    print("\n1. 创建测试DID:")
    test_did = DID.create(did_type="test")
    print(f"   生成: {test_did}")
    
    print("\n2. 解析测试:")
    parsed = DID.parse("did:xca:device:sensor_001")
    print(f"   解析成功: {parsed}")
    
    print("\n3. 生成文档:")
    doc = test_did.generate_document()
    print(f"   文档ID: {doc['id']}")
    
    print("\n" + "=" * 50)
    print("🎉 基本功能验证通过！")
    
except ImportError as e:
    print(f"❌ 导入失败: {e}")
    print("\n解决方案:")
    print("1. 确保存在 src/__init__.py 文件")
    print("2. 确保存在 src/core/__init__.py 文件")
    
except Exception as e:
    print(f"❌ 错误: {type(e).__name__}: {e}")
```
