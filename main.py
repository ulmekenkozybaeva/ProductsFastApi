from fastapi import FastAPI

app = FastAPI()

@app.get("/AllProducts")
def root():
    return {'LG fridge':'Smart Inverter',
            'LG washing machine':'TurboWash59, ThinQ',
            'LG monitors':'27'' IPS Full HD',
            'Samsung telephone':'Galaxy S23 Ultra',
            'Samsung TV':'Neo QLED 4K QN90C',
            'Samsung Monitor':'Odyssey Neo G9 Dual 4K Curved Gaming Monitor',
            'Apple telephone':'iPhone 15 Pro Max 5G',
            'Apple watch':'Series 6 Cellular Gold Stainleess Steel M07P3',
            'Apple headphone':'AirPods Max'}

@app.get("/allproducts")
def root():
    json_products = jsonable_encoder(products)
    return JSONResponse(content=json_products)

@app.get("/AllProducts/{brand}")
def get_products_by_brand(brand: str):
    if brand in products:
        return {"products": products[brand]}
    raise HTTPException(status_code=404, detail="Brand not found")