"""Test Text Summarization module"""

import unittest

from pororo import Pororo


class PororoSummarizationTester(unittest.TestCase):

    def test_modules(self):
        summarization = Pororo(
            task="summarization",
            lang="ko",
            model="extractive",
        )
        summarization_res = summarization(
            "올해 8월 17일이 임시공휴일로 지정된다. 정세균 국무총리가 지난 19일 코로나19 장기화로 지친 의료진과 국민들의 휴식 및 내수 활성화를 위해 검토를 지시한지 이틀만이다. 정부는 21일 문재인 대통령 주재로 국무회의를 열어 '8월 17일 임시공휴일 지정안'을 의결했다고 밝혔다. 이에 따라 인사혁신처는 대통령 재가, 관보 공고 등 임시공휴일 확정을 위한 후속 조치에 착수하는 한편, 공휴일 지정으로 인해 관공서 민원실, 어린이집 운영 등에 있어 국민 불편이 없도록 관계 부처가 사전 대책을 마련하도 록 요청할 예정이다. 이번 임시공휴일은 관공서 뿐 아니라 근로기준법상 상시 300명  이상 근로자를 둔 사업장에 적용된다. 임시공휴일은 국가적인 행사를 기념하거나 내수 진작 등의 필요에 따라 정부에서 지정하는 공휴일이다. 올해 8월 17일 임시공휴일 지정은 코로나19 장기화로 인한 국민들의 높은 피로감 및 어려운 경제상황을 고려한 내 수 진작 등을 감안해 추진됐다. 올해 3.1절, 현충일, 광복절, 개천절 등 법정공휴일이 주말과 겹쳐 국민들의 휴식 기회가 적은 점도 지정 결정에 영향을 미쳤다. 최근에는 2017년 10월 2일(추석 연휴 전날), 2017년 5월 9일(제19대 대통령선거일), 2016년 5월 6일(어린이날 다음날), 2015년 8월 14일(광복절 전날)이 임시공휴일로 지정됐다."
        )
        self.assertIsInstance(summarization_res, str)

        summarization = Pororo(
            task="summarization",
            lang="ko",
            model="abstractive",
        )
        summarization_res = summarization(
            "올해 8월 17일이 임시공휴일로 지정된다. 정세균 국무총리가 지난 19일 코로나19 장기화로 지친 의료진과 국민들의 휴식 및 내수 활성화를 위해 검토를 지시한지 이틀만이다. 정부는 21일 문재인 대통령 주재로 국무회의를 열어 '8월 17일 임시공휴일 지정안'을 의결했다고 밝혔다. 이에 따라 인사혁신처는 대통령 재가, 관보 공고 등 임시공휴일 확정을 위한 후속 조치에 착수하는 한편, 공휴일 지정으로 인해 관공서 민원실, 어린이집 운영 등에 있어 국민 불편이 없도록 관계 부처가 사전 대책을 마련하도 록 요청할 예정이다. 이번 임시공휴일은 관공서 뿐 아니라 근로기준법상 상시 300명  이상 근로자를 둔 사업장에 적용된다. 임시공휴일은 국가적인 행사를 기념하거나 내수 진작 등의 필요에 따라 정부에서 지정하는 공휴일이다. 올해 8월 17일 임시공휴일 지정은 코로나19 장기화로 인한 국민들의 높은 피로감 및 어려운 경제상황을 고려한 내 수 진작 등을 감안해 추진됐다. 올해 3.1절, 현충일, 광복절, 개천절 등 법정공휴일이 주말과 겹쳐 국민들의 휴식 기회가 적은 점도 지정 결정에 영향을 미쳤다. 최근에는 2017년 10월 2일(추석 연휴 전날), 2017년 5월 9일(제19대 대통령선거일), 2016년 5월 6일(어린이날 다음날), 2015년 8월 14일(광복절 전날)이 임시공휴일로 지정됐다."
        )
        self.assertIsInstance(summarization_res, str)

        summarization = Pororo(
            task="summarization",
            lang="ko",
            model="bullet",
        )
        summarization_res = summarization(
            "올해 8월 17일이 임시공휴일로 지정된다. 정세균 국무총리가 지난 19일 코로나19 장기화로 지친 의료진과 국민들의 휴식 및 내수 활성화를 위해 검토를 지시한지 이틀만이다. 정부는 21일 문재인 대통령 주재로 국무회의를 열어 '8월 17일 임시공휴일 지정안'을 의결했다고 밝혔다. 이에 따라 인사혁신처는 대통령 재가, 관보 공고 등 임시공휴일 확정을 위한 후속 조치에 착수하는 한편, 공휴일 지정으로 인해 관공서 민원실, 어린이집 운영 등에 있어 국민 불편이 없도록 관계 부처가 사전 대책을 마련하도 록 요청할 예정이다. 이번 임시공휴일은 관공서 뿐 아니라 근로기준법상 상시 300명  이상 근로자를 둔 사업장에 적용된다. 임시공휴일은 국가적인 행사를 기념하거나 내수 진작 등의 필요에 따라 정부에서 지정하는 공휴일이다. 올해 8월 17일 임시공휴일 지정은 코로나19 장기화로 인한 국민들의 높은 피로감 및 어려운 경제상황을 고려한 내 수 진작 등을 감안해 추진됐다. 올해 3.1절, 현충일, 광복절, 개천절 등 법정공휴일이 주말과 겹쳐 국민들의 휴식 기회가 적은 점도 지정 결정에 영향을 미쳤다. 최근에는 2017년 10월 2일(추석 연휴 전날), 2017년 5월 9일(제19대 대통령선거일), 2016년 5월 6일(어린이날 다음날), 2015년 8월 14일(광복절 전날)이 임시공휴일로 지정됐다."
        )
        self.assertIsInstance(summarization_res, list)


if __name__ == "__main__":
    unittest.main()