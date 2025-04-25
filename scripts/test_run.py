from app.services.llm_service import generate_sql, generate_docs

if __name__ == "__main__":
    sql_prompt = "Get the top 10 products by sales from orders table"
    print("Generated SQL:\n", generate_sql(sql_prompt))

    spark_code = """
    val topProducts = orders
      .groupBy("product_id")
      .agg(sum("sales").alias("total_sales"))
      .orderBy(desc("total_sales"))
      .limit(10)
    """
    print("\nGenerated Documentation:\n", generate_docs(spark_code))
