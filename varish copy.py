import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataLoader:
    """Loads sales data from a CSV file into a pandas DataFrame."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_data(self) -> pd.DataFrame:
        try:
            self.data = pd.read_csv(self.filepath, parse_dates=["Date"])
            self.data["Revenue"] = self.data["UnitsSold"] * self.data["UnitPrice"]
            print(f"[DataLoader] Loaded {len(self.data)} rows from {self.filepath}")
            return self.data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.filepath}")

    def preview(self, rows: int = 5):
        print(self.data.head(rows))


class SalesAnalyzer:
    """Performs statistical analysis on sales data using pandas & numpy."""

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def total_revenue(self) -> float:
        return np.sum(self.data["Revenue"])

    def average_units_sold(self) -> float:
        return np.mean(self.data["UnitsSold"])

    def revenue_by_category(self) -> pd.Series:
        return self.data.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

    def revenue_by_region(self) -> pd.Series:
        return self.data.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

    def monthly_revenue_trend(self) -> pd.Series:
        temp = self.data.copy()
        temp["Month"] = temp["Date"].dt.to_period("M")
        return temp.groupby("Month")["Revenue"].sum()

    def top_products(self, n: int = 3) -> pd.Series:
        return self.data.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(n)

    def summary_stats(self) -> pd.DataFrame:
        return self.data[["UnitsSold", "UnitPrice", "Revenue"]].describe()


class SalesVisualizer:
    """Creates visualizations from analyzed sales data using matplotlib."""

    def __init__(self, analyzer: SalesAnalyzer):
        self.analyzer = analyzer

    def plot_revenue_by_category(self):
        data = self.analyzer.revenue_by_category()
        plt.figure(figsize=(7, 5))
        data.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Revenue by Category")
        plt.ylabel("Revenue (₹)")
        plt.xlabel("Category")
        plt.tight_layout()
        plt.savefig("revenue_by_category.png")
        plt.close()
        print("[Visualizer] Saved revenue_by_category.png")

    def plot_monthly_trend(self):
        data = self.analyzer.monthly_revenue_trend()
        plt.figure(figsize=(7, 5))
        data.plot(kind="line", marker="o", color="green")
        plt.title("Monthly Revenue Trend")
        plt.ylabel("Revenue (₹)")
        plt.xlabel("Month")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("monthly_revenue_trend.png")
        plt.close()
        print("[Visualizer] Saved monthly_revenue_trend.png")

    def plot_region_pie(self):
        data = self.analyzer.revenue_by_region()
        plt.figure(figsize=(6, 6))
        plt.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
        plt.title("Revenue Share by Region")
        plt.tight_layout()
        plt.savefig("revenue_by_region.png")
        plt.close()
        print("[Visualizer] Saved revenue_by_region.png")


class SalesReport:
    """Combines loading, analysis, and visualization into one report."""

    def __init__(self, filepath: str):
        self.loader = DataLoader(filepath)
        self.data = self.loader.load_data()
        self.analyzer = SalesAnalyzer(self.data)
        self.visualizer = SalesVisualizer(self.analyzer)

    def generate(self):
        print("\n===== SALES REPORT =====")
        print(f"Total Revenue: ₹{self.analyzer.total_revenue():,.2f}")
        print(f"Average Units Sold per Transaction: {self.analyzer.average_units_sold():.2f}")

        print("\nRevenue by Category:")
        print(self.analyzer.revenue_by_category())

        print("\nRevenue by Region:")
        print(self.analyzer.revenue_by_region())

        print("\nTop 3 Products by Revenue:")
        print(self.analyzer.top_products())

        print("\nSummary Statistics:")
        print(self.analyzer.summary_stats())

        self.visualizer.plot_revenue_by_category()
        self.visualizer.plot_monthly_trend()
        self.visualizer.plot_region_pie()
        print("\n[Report] All charts generated successfully.")


if __name__ == "__main__":
    report = SalesReport("sales_data.csv")
    report.generate()
