import sktime
from sktime.datasets import load_airline
from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.forecasting.theta import ThetaForecaster
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error

print("sktime version: ", sktime.__version__)
# 航空会社の単変量時系列データセットをロード
y = load_airline()
# シャッフルなしでtrainとtestに分割
y_train, y_test = temporal_train_test_split(y)
print(y_train)
# Forecasting horizon
fh = ForecastingHorizon(y_test.index, is_relative=False)
# シータ法適用
forecaster = ThetaForecaster(sp=12)  # monthly seasonal periodicity
forecaster.fit(y_train)
y_pred = forecaster.predict(fh)
# 平均絶対パーセント誤差(MAPE)算出
mape = mean_absolute_percentage_error(y_test, y_pred)
print("MAPE:", mape)